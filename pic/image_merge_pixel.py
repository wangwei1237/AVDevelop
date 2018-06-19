#encoding=utf8

from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt 

im1 = np.array(Image.open('1.png'))
im2 = np.array(Image.open('2.png'))
im3 = np.array(Image.open('3.png'))

im3 = im1 + im2 

plt.subplot(221)
plt.axis('off')
plt.imshow(im1)

plt.subplot(222)
plt.axis('off')
plt.imshow(im2)

plt.subplot(223)
plt.axis('off')
plt.imshow(im3)

plt.show()



