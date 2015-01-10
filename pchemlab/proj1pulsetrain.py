# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:49:54 2014

@author: Haina
"""
import matplotlib
import numpy as np
import math


freq = 2e9
samplingrate = 24e9
shift = math.pi #shift by this amount, change to zero for no shift
timeinterval = 1/samplingrate
bposition = 20e-9
cstd = 4.2466e-8
trainnum = 50 #how many pulses in the train
points = 20000*12
FWHM =  2.355*cstd #not a variable, for reference

values = np.zeros((points, 2))
gauss = np.zeros((points, 1))
for i in range(points):
    values[i,0] = i*timeinterval
for cycle in range(trainnum):
    for point in range(points/trainnum):
        gauss[point+cycle*points/trainnum] = math.exp(-math.pow((values[point,0]-bposition),2)/(2*math.pow(cstd,2)))

        values[point+cycle*points/trainnum,1] = gauss[point+cycle*points/trainnum]*math.sin(2*math.pi*freq*values[point,0] + shift)

        



#matplotlib.pyplot.plot(values[:,0], values[:,1])
#matplotlib.pyplot.plot(values[:,0], values[:,1])
#matplotlib.pyplot.xlabel('Time (seconds)')
#matplotlib.pyplot.ylabel('Intensity')
#matplotlib.pyplot.show()

outputname = 'pulsetrain2.txt'
f = open(outputname, 'w')
for i in range(np.shape(values)[0]):
    f.write(str(values[i,1]) + '\n')
    
f.close()


