import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os

filecount = 10 
interval = 2.5e-10

for file in os.listdir('E:\\chem 3821\\Nutrationdata\\'):
    if file.endswith("OCS_nutation" + str(filecount) + "_130us_10mTneon_500mV_TUESDAY_8.txt"):

        path_to_file = os.path.abspath('E:\\chem 3821\\Nutrationdata\\' + file) 
        print "Processing ", file 
        f = np.loadtxt(path_to_file)
        xvalues = np.arange(0, interval*len(f)-interval, interval)+(1e-5*filecount)
        yvalues = f
        

        
        plt.plot(xvalues, yvalues)
        
        filecount = filecount + 1
        
plt.xlabel('Time (seconds)')
plt.ylabel('Intensity')
matplotlib.pylab.show();