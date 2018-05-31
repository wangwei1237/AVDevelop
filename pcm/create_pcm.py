#!encoding=utf-8
import math
import struct
import os

'''
@brief: this file used for generate a 5s sample sound infomation.
         the sound frequency is 440Hz, the sample rate is 44100, the channel is 1.
'''

if os.path.exists("test.pcm"):
	os.remove("test.pcm")

if os.path.exists("test1.pcm"):
	os.remove("test1.pcm")

sample_rate = 44100.0
duration    = 10.0
nb_samples  = sample_rate * duration

samples = []

tincr   = 2 * math.pi * 440.0 / sample_rate
angle   = 0

for i in xrange(int(nb_samples)):
	ampliltute     = math.sin(angle)
	samples.append(int(ampliltute * 32767))
	angle += tincr

#print samples

#print samples[1]
#print struct.pack("<1h", samples[0])
file = open("test.pcm", 'a+')
for i in xrange(len(samples)):
	file.write(struct.pack("<1h", samples[i]))
	

samples_1 = []
angle     = 0
for i in xrange(int(nb_samples)):
	ampliltute     = (math.sin(angle) + math.sin(angle *2 + math.pi / 3)
	                +math.sin(angle * 3 + math.pi / 2) + math.sin(angle * 4 + math.pi / 4)) * 0.25
	samples_1.append(int(ampliltute * 32767))
	angle += tincr

file_1 = open("test1.pcm", 'a+')
for i in xrange(len(samples_1)):
	file_1.write(struct.pack("<1h", samples_1[i]))

file.close()
file_1.close()
