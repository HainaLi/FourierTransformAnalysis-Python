# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 21:11:47 2014

@author: Haina
"""
import matplotlib
import numpy as np
import os

path_to_file = os.path.abspath('C:\Users\Haina\Desktop\chem 3821\Tuesdaydetuning.txt') #this sets the path to the file that you want to open
data = np.loadtxt(path_to_file)


datasize = len(data)

interval = 2.5e-10
pulsenum = 25
pulse = 2000000
belowpulsenum = 1000


timevalues = np.zeros((datasize, 1))

for i in range(datasize):
    if (i == 0):
        timevalues[i] = 0
    else:
        timevalues[i] = timevalues[i-1] + interval

matplotlib.pyplot.plot(timevalues,data)
matplotlib.pyplot.xlabel('Time (seconds)')
matplotlib.pyplot.ylabel('Intensity')
matplotlib.pylab.show();

pulseduration = []
track = 0
belowpulse = 0
start = 0.0
end = 0.0
difference = 0 
pulsecount = 0 
continuouspulse = 0 
startend = np.zeros((25, 2))

for j in range(19000, datasize):
    if ((data[j] > pulse) & (track == 0)): #indicates that pulse started
        print "pulse started at time: ", timevalues[j], "intensity of ", data[j]
        start = timevalues[j]
        track = track + 1 #indicates that the pulse started 
        startend[pulsecount][0] = j 
    if ((data[j] < pulse) & (track != 0)) :
        belowpulse = belowpulse + 1 
        #print "belowpulse: ", belowpulse
    else:
        belowpulse = 0 
    if ((belowpulse == belowpulsenum) & (track != 0) ):
        print "pulse ended at time: ", timevalues[j + 1 - belowpulsenum]
        startend[pulsecount][1] = j + 1 - belowpulsenum
        pulsecount = pulsecount + 1
        end = timevalues[j + 1 - belowpulsenum]
        pulseduration.append((end - start)[0])
        belowpulse = 0 
        track = 0 
    
print "Pulse Durations: ", pulseduration
print "Pulse Count: ", pulsecount
print "Start and end indices: ", startend
        
        

       