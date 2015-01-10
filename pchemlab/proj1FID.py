# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:49:54 2014

@author: Haina
"""

from matplotlib import pyplot as plt
import numpy as np
import math

timeinterval = 5e-10
freq = 100e6
tau = 100e-9
D = 100e-9
points = 100000



values = np.zeros((points, 2))
singledecay = np.zeros((points, 1))
dopplerdecay = np.zeros((points,1))
for i in range(points):
    values[i,0] = i*timeinterval
    singledecay[i] = math.exp(-values[i,0]/tau)
    dopplerdecay[i] = math.exp(-1*values[i,0]**2/D**2)

    
for j in range (points):
    values[j,1] = singledecay[j]*math.sin(2*math.pi*freq*values[j,0])
    #values[j,1] = dopplerdecay[j]*math.sin(2*math.pi*freq*values[j,0])

plt.plot(values[:,0], dopplerdecay[:])
plt.plot(values[:,0], values[:,1], 'red',linewidth=0.8)
plt.xlabel('Time (seconds)')
plt.ylabel('Intensity')
plt.grid(True)

plt.show()


'''outputname = 'Dopplerdecay100nsTRIAL.TXT'
f = open(outputname, 'w')
for i in range(np.shape(values)[0]):
    f.write(str(str(values[i,1]) + '\n'))
    
f.close()'''

