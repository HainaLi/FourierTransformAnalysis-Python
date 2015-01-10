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
points = 200*10

values = np.zeros((10000, 2))
for i in range(10000):
    values[i,0] = i*timeinterval
for j in range (points):
    values[j+6000,1] = math.sin(2*math.pi*freq*values[j,0])



matplotlib.pyplot.scatter(values[:,0], values[:,1])
matplotlib.pyplot.show()

    
f.close()
