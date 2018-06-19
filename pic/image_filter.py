#encoding=utf-8

from PIL import Image
from PIL import ImageFilter

imgF = Image.open('1.jpg')
#imgF.show()
outF = imgF.filter(ImageFilter.CONTOUR)
outF.show()

