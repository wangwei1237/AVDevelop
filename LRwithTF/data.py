#encoding=utf-8

import numpy as np 
import matplotlib.pyplot as plt 

x1_label1 = np.random.normal(3, 1, 1000)
x2_label1 = np.random.normal(2, 1, 1000)
x1_label2 = np.random.normal(7, 1, 1000)
x2_label2 = np.random.normal(6, 1, 1000)

x1s = np.append(x1_label1, x1_label2)
x2s = np.append(x2_label1, x2_label2)

ys  = np.asarray([0.] * len(x1_label1) + [1.] * len(x1_label2))


def _draw_data(x11, x12, x21, x22):
	plt.scatter(x11, x12, marker='x', c='r', s=20)
	plt.scatter(x21, x22, marker='o', c='g', s=20)
	plt.show()

if __name__ == '__main__':
	_draw_data(x1_label1, x2_label1, x1_label2, x2_label2)


