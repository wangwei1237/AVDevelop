#!encoding=utf-8

import apiutil
from PIL import Image
import json

AppID  = '1106954466'
AppKey = '5u6ehLVCgxhznKhX'

ai_obj = apiutil.AiPlat(AppID, AppKey)
with open('1.png', 'rb') as bin_data:
    image_data = bin_data.read()

#rsp = ai_obj.getFaceInfo(image_data, 0)
rsp = ai_obj.getOcrGeneralocr(image_data)
print json.dumps(rsp)

exit()
if rsp['ret'] == 0:
    beauty = 0
    
    for face in rsp['data']['face_list']:
        #print(face)
        face_area = (face['x'], face['y'], face['x'] + face['width'], face['y'] + face['height'])
        #print(face_area)
        img = Image.open("1.png")
        cropped_img = img.crop(face_area).convert('RGB')
        cropped_img.save('data/' + face['face_id'] + '.png')
