# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 01:03:00 2014

@author: Haina
"""
import os
import matplotlib
import numpy as np

path_to_file = os.path.abspath('C:\Users\Haina\Desktop\chem 3821\decay.txt') #this sets the path to the file that you want to open
signal = np.genfromtxt(path_to_file)



answer = np.fft.fft2(signal)

print answer

time = answer[:,0]
intensity = answer[:,1]
print intensity
matplotlib.pyplot.scatter(time.real,intensity.real)
    
matplotlib.pyplot.xlabel('Frequency')
matplotlib.pyplot.ylabel('Intensity')
matplotlib.pylab.show();