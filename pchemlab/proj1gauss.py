# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:49:54 2014

@author: Haina
"""

import matplotlib
import numpy as np
import scipy.stats
import math

timeinterval = 5e-10
freq = 100e6
bposition = 2.5e-6
cstd = .42466e-7
offset = 0
points = 10000
FWHM =  2.355*cstd

values = np.zeros((10000, 2))
gauss = np.zeros((points, 1))
gausssize = np.shape(gauss)[0]
for i in range(10000):
    values[i,0] = i*timeinterval
for k in range(points):
    #xvalues = np.linspace(-1, 1, points)
    gauss[k] = math.exp(-math.pow((values[k+offset,0]-bposition),2)/(2*math.pow(cstd,2)))
for j in range (points):
    values[j,1] = gauss[j]*math.sin(2*math.pi*freq*values[j,0])


#matplotlib.pyplot.plot(xvalues, gauss[:,0])
matplotlib.pyplot.plot(values[:,0], values[:,1], 'blue', linewidth=0.8)
matplotlib.pyplot.xlabel('time (seconds)')
matplotlib.pyplot.ylabel('intensity')
matplotlib.pyplot.show()

outputname = 'gausswave500ns.txt'
f = open(outputname, 'w')
for i in range(np.shape(values)[0]):
    f.write(str(values[i,1]) + '\n')
    
f.close()

