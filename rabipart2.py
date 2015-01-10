# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 23:40:14 2014

@author: Haina
"""

import matplotlib as plt
import numpy as np
import os
import scipy



        
#start of main
path_to_file = os.path.abspath('C:\Users\Haina\Desktop\chem 3821\Nutration datadetuningindices.txt') #this sets the path to the file that you want to open
indices = np.loadtxt(path_to_file)


start = indices[:,0]
end = indices[:,1]

endcutamount = 500
startcutamount = 200 #delay number of points


datasize = len(data)

interval = 2.5e-10
pulsenum = 25

timevalues = np.zeros((datasize, 1))

for i in range(datasize):
    if (i == 0):
        timevalues[i] = 0
    else:
        timevalues[i] = timevalues[i-1] + interval

for i in range(pulsenum):
    if (i == 24):
        time = timevalues[end[i]+startcutamount:datasize-1:1]
        signal = data[end[i]+startcutamount:datasize-1:1]
    else:
        time = timevalues[end[i]+startcutamount:start[i+1]-endcutamount:1]
        signal = data[end[i]+startcutamount:start[i+1]-endcutamount:1]
    
    f = 'C:\Users\Haina\Desktop\chem 3821\decaydata\decay' + str(i) + '.txt'
    path_to_outfile=os.path.abspath(f)
    f=open(path_to_outfile, 'a')
    for i in range(len(signal)):
        f.write(str(signal[i]) + '\n')
    f.close()
    
    
    #matplotlib.pyplot.plot(time,signal)
    
#matplotlib.pyplot.xlabel('Time (seconds)')
#matplotlib.pyplot.ylabel('Intensity')
#matplotlib.pylab.show();


#f = 'decay.txt'
#path_to_outfile=os.path.abspath("C:\\Users\\Haina\\Desktop\\chem 3821\\" + f)
#f=open(path_to_outfile, 'a')
#for i in range(len(signal)):
#    f.write(str(signal[i]) + '\n')
#f.close()