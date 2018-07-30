#encoding=utf-8

from PIL import Image
from PIL import ImageFilter

def sketch(img, threshold):
    '''
    素描
    param img: Image实例
    param threshold: 介于0到100
    '''
    if threshold < 0: threshold = 0
    if threshold > 100: threshold = 100
     
    width, height = img.size
    img = img.convert('L') # convert to grayscale mode
    pix = img.load() # get pixel matrix
 
    for w in xrange(width):
        for h in xrange(height):
            if w == width-1 or h == height-1:
                continue
             
            src = pix[w, h]
            dst = pix[w+1, h+1]
 
            diff = abs(src - dst)
 
            if diff >= threshold:
                pix[w, h] = 0
            else:
                pix[w, h] = 255
 
    return img

imgF = Image.open('2.jpg')
#imgF.show()
outF = imgF.filter(ImageFilter.CONTOUR)
#outF.show()
#imgF.show()
#imgO = sketch(imgF, 17)
outF.show()

