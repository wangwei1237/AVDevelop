//
//  ViewController.swift
//  MetalTriangle
//
//  Created by wangwei on 2018/10/8.
//  Copyright © 2018 wangwei. All rights reserved.
//

import UIKit
import Metal
import QuartzCore

class ViewController: UIViewController {
    //[[ properties
    var device:MTLDevice!                     = nil
    var metalLayer:CAMetalLayer!              = nil
    var vertexBuffer:MTLBuffer!               = nil
    var pipelineState:MTLRenderPipelineState! = nil
    var commandQueue:MTLCommandQueue!         = nil
    var timer:CADisplayLink!                  = nil
    
    let vertexData:[Float] = [
         0.0,  0.5, 0.0,
        -0.5, -0.5, 0.0,
         0.5, -0.5, 0.0,
        -1.0,  0.5, 0.0,
        -0.5, -0.5, 0.0,
         0.0,  0.5, 0.0,
    ]
    //]]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view, typically from a nib.
        
        initMTLDevice()
        initMTLLayer()
        initVertexBuffer()
        initPipelineState()
        initCommandQueue()
        
        timer = CADisplayLink(target: self, selector: #selector(drawloop))
        timer.add(to: RunLoop.main, forMode: RunLoop.Mode.default)
    }
    
    func initMTLDevice() {
        self.device = MTLCreateSystemDefaultDevice()
    }
    
    func initMTLLayer() {
        self.metalLayer = CAMetalLayer()
        
        self.metalLayer.device      = self.device
        self.metalLayer.pixelFormat = .bgra8Unorm
        metalLayer.framebufferOnly  = true
        metalLayer.frame            = view.layer.frame
        
        var drawableSize        = self.view.bounds.size
        drawableSize.height    -= UIApplication.shared.statusBarFrame.size.height
        drawableSize.width     *= self.view.contentScaleFactor
        drawableSize.height    *= self.view.contentScaleFactor
        metalLayer.drawableSize = drawableSize
        
        self.view.layer.addSublayer(metalLayer)
    }
    
    func initVertexBuffer() {
        let dataSize      = self.vertexData.count * MemoryLayout<Float>.size
        self.vertexBuffer = device.makeBuffer(bytes: vertexData, length: dataSize, options: MTLResourceOptions(rawValue: UInt(0)))
    }
    
    func initPipelineState() {
        let defaultLibrary = self.device.makeDefaultLibrary()
        let vertexFunc     = defaultLibrary?.makeFunction(name: "basic_vertex")
        let fragmentFunc   = defaultLibrary?.makeFunction(name: "basic_fragment")
        let pipelineDescriptor = MTLRenderPipelineDescriptor()
        pipelineDescriptor.vertexFunction   = vertexFunc
        pipelineDescriptor.fragmentFunction = fragmentFunc
        pipelineDescriptor.colorAttachments[0].pixelFormat = .bgra8Unorm
        
        do {
            try self.pipelineState = self.device.makeRenderPipelineState(descriptor: pipelineDescriptor)
        } catch {
            
        }
    }
    
    func initCommandQueue() {
        self.commandQueue = self.device.makeCommandQueue()
    }
    
    @objc func drawloop() {
        self.render()
    }
    
    func render() {
        // metal layer上调用nextDrawable() ，它会返回你需要绘制到屏幕上的纹理(texture)
        let drawable = metalLayer.nextDrawable()
        
        // 创建一个Render Pass Descriptor，配置什么纹理会被渲染到、clear color，以及其他的配置
        let renderPassDesciptor = MTLRenderPassDescriptor()
        renderPassDesciptor.colorAttachments[0].texture = drawable?.texture
        // 设置load action为clear，也就是说在绘制之前，把纹理清空
        renderPassDesciptor.colorAttachments[0].loadAction = .clear
        // 绘制的背景颜色设置为绿色
        renderPassDesciptor.colorAttachments[0].clearColor = MTLClearColorMake(0.0, 0.8, 0.5, 1.0)
        
        let commandBuffer = commandQueue.makeCommandBuffer()
        // 创建一个渲染命令编码器(Render Command Encoder)
        // 创建一个command encoder，并指定你之前创建的pipeline和顶点
        let renderEncoder = commandBuffer?.makeRenderCommandEncoder(descriptor: renderPassDesciptor)
        renderEncoder?.setRenderPipelineState(pipelineState)
        renderEncoder?.setVertexBuffer(vertexBuffer, offset: 0, index: 0)
        renderEncoder?.drawPrimitives(type: .triangle, vertexStart: 0, vertexCount: 6, instanceCount: 2)
        renderEncoder?.endEncoding()
        
        commandBuffer?.present(drawable!)
        commandBuffer?.commit()
    }
}
