#encoding=utf-8

import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf 

import data as d 

learn_rate = 0.3
epochs     = 10000

X1 = tf.placeholder(tf.float32, shape=(None,), name='x1')
X2 = tf.placeholder(tf.float32, shape=(None,), name='x2')
Y  = tf.placeholder(tf.float32, shape=(None,), name='y')
W  = tf.Variable([0., 0., 0.], name='w', trainable='True')

Y_       = tf.sigmoid(W[2] * X2 + W[1] * X1 + W[0])
cost     = tf.reduce_mean(-tf.log((Y * Y_) + (1-Y) * (1-Y_)))
train_op = tf.train.GradientDescentOptimizer(learn_rate).minimize(cost)

value_w = [0.] * 3

with tf.Session() as sess:
	init = tf.global_variables_initializer()
	sess.run(init)

	prev_error = 0.
	for epoch in xrange(epochs):
		err, _ = sess.run([cost, train_op], feed_dict={X1:d.x1s, X2:d.x2s, Y:d.ys})
		print "epoch: %d, error: %f" % (epoch, err)
		if abs(prev_error - err) < 0.0001:
			break

		prev_error = err

	value_w = sess.run(W)

	print "[%f, %f, %f]" % (value_w[0], value_w[1], value_w[2])

def sigmoid(x):
	return 1.0 / (1.0 + np.exp(-x))  


x1_b, x2_b = [], []
for x1 in np.linspace(0, 10, 100):
	for x2 in np.linspace(0, 10, 100):
		z = sigmoid(x2 * value_w[2] + x1 * value_w[1] + value_w[0])
		'''
		绘制分类平面 
		'''
		if abs(z - 0.5) < 0.01: 
			x1_b.append(x1)
			x2_b.append(x2)

plt.scatter(x1_b, x2_b, c='b', marker='o')
plt.scatter(d.x1_label1, d.x2_label1, c='r', marker='x')
plt.scatter(d.x1_label2, d.x2_label2, c='g', marker='1')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
