'''
Created on 29/03/2012

@author: Cristobal
'''
import os
import numpy as np
import math
import scipy.fftpack
from matplotlib import pyplot as plt

samplerate=1E9 #this is the sample rate (digitization rate) of the digitizer that was used

path_to_file = os.path.abspath('C:\Users\Haina\My Documents\Python Scripts\pchemlab\pulsetrain2.txt') #this sets the path to the file that you want to open
f=open(path_to_file) #this opens the file and reads the time domain data that you collected on the scope
timedomain=[] #this creates a list to put our data in
for row in f: #this for loop goes through and splits out the data so that we can analyze it
    temp=row.split()
    #print row
    timedomain.append(float(temp[np.size(temp)-1]))

ndata=size(timedomain) #determines how many points the scope collected 

temp=np.zeros(ndata*2) #creates an array of zeros twice the size of the nubmer of points
temp[0:ndata]=timedomain #this puts the time domain data into the array
timepad=temp #this is used to "pad" the array with zeros. it allows us to get a better resolution for our spectrum

fft=abs(scipy.fftpack.fft(timepad))/100 #this module FFTs the data and takes the absolute value of the data (giving us the magnitude FT)
freq=(scipy.fftpack.fftfreq(size(timepad),1/samplerate))/1E6 #This creates the frequency array that matches with the intensity values of the fft

print np.size(fft)
print np.size(freq)

out=np.zeros((np.size(freq),2)) #this creates an array to combine the intensity values and the frequencies

for i, row in enumerate(freq): #this for loop combines them and removes any frequencies we don't want
        if row>=4 and row<200:
				out[i,0] = row
				out[i,1] = fft[i]




f = np.savetxt(path_to_file[:-4] + '_FT.txt',out) #this saves your data
plt.plot(out[:,0],out[:,1]) #these commands plot our data
plt.xlabel('Frequency (MHz)')
plt.ylabel('Intensity (mV)')
#plt.title('Spectrum')
plt.grid(True)
plt.show()