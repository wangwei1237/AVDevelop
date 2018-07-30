#encoding=utf8

from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt 

im1 = np.array(Image.open('1.jpg').convert('L'))
im2 = im1.copy()

rows, cols = im2.shape
for i in xrange(rows):
	for j in xrange(cols):
		if (im2[i,j] > 128):
			im2[i,j] = 1
		else:
			im2[i,j] = 0

plt.subplot(211)
plt.axis('off')
plt.imshow(im1)

plt.subplot(212)
plt.axis('off')
plt.imshow(im2)

plt.show()



