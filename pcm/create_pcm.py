#!encoding=utf-8
import math
import struct
import os

'''
@brief: this file used for generate a 5s sample sound infomation.
         the sound frequency is 440Hz, the sample rate is 44100, the channel is 1.
'''

f1 = "test1.pcm"
f2 = "test2.pcm"

if os.path.exists(f1):
	os.remove(f1)

if os.path.exists(f2):
	os.remove(f2)

sample_rate = 44100.0
duration    = 10.0
nb_samples  = sample_rate * duration
tincr       = 2 * math.pi * 440.0 / sample_rate 

samples = []
angle   = 0
for i in xrange(int(nb_samples)):
	ampliltute     = math.sin(angle)
	samples.append(int(ampliltute * 32767))
	angle += tincr

file = open(f1, 'a+')
for i in xrange(len(samples)):
	file.write(struct.pack("<1h", samples[i]))
file.close()

samples_1 = []
angle     = 0
for i in xrange(int(nb_samples)):
	ampliltute     = (math.sin(angle) + math.sin(angle *2 + math.pi / 3)
	                +math.sin(angle * 3 + math.pi / 2) + math.sin(angle * 4 + math.pi / 4)) * 0.25
	samples_1.append(int(ampliltute * 32767))
	angle += tincr

file_1 = open(f2, 'a+')
for i in xrange(len(samples_1)):
	file_1.write(struct.pack("<1h", samples_1[i]))
file_1.close()
