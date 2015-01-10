# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 12:58:17 2014

@author: mmwavecat
"""

import numpy as np
from matplotlib import pyplot as plt
import os

Shots = 1e4
DigRate = 4.000
ExpNum = 26
Exptime = 5e-6  

class ScopeTrace(object):
    def __init__(self, VScale = 1, Acquiris = False, TiePie = False, TiePie2 = False, overwrite = 'no',\
    Timetrace=[],Metadata=[]):
        self.Acquiris = Acquiris
        self.TiePie = TiePie
        self.TiePie2 = TiePie2
        self.overwrite = overwrite
        self.Timetrace = Timetrace
        self.Metadata = Metadata
        self.VScale = VScale
    
    def openit(self,filename):
    
        self.filename = filename
        del self.Timetrace
        self.Timetrace = []
        
        f=open(filename,'r')       
        count = 0
        for row in f:
            if row[0] == 'A':
                self.TiePie = True 
            if row[0] == 'C':
                self.TiePie2 = True
            if row[0] == '$':
                if count >=3:
                    data=row.split()
                    self.Metadata.append(float(data[1]))
            if row[0]!='$' and row[0]!='#' and self.TiePie == False and self.TiePie2 == False:
            #Allows us to read in from Tek scopes
                if row[0]=='"':        
                    data=row.split()
                    self.Timetrace.append(float(data[len(data)-1]))
                else:
                    data=row.split()
                    self.Timetrace.append(float(data[len(data)-1]))
            elif self.TiePie == True:
                if count >= 9:
                    data=row.split()
                    self.Timetrace.append(float(data[len(data)-1]))
            elif self.TiePie2 == True:
                if count >= 1:
                    data=row.split()
                    self.Timetrace.append(float(data[0]))
    # Reads in Agilent card data
            else:
                self.Acquiris = True
            count += 1
        self.Timetrace = np.array(self.Timetrace)
        return self.Timetrace
        
    def bin_to_voltage(self,Shots):#,Timetrace):
        self.Shots = Shots
        
        Fullscale=self.Metadata[0]
        ChannelFSR=self.Metadata[2]
        VScale1=Fullscale/ChannelFSR
        
        if VScale1 >= 51 and VScale1 <=52:
            self.VScale= 5.0        
        if VScale1 >= 128 and VScale1 <=129:
            self.VScale= 2.0
        if VScale1 >= 256 and VScale1 <=257:
            self.VScale= 1.0
        if VScale1 >= 512 and VScale1 <= 513:
            self.VScale = 0.5
        if VScale1 >= 1280 and VScale1 <= 1281:
            self.VScale=0.2
        if VScale1 >= 2560 and VScale1 <= 2561:
            self.VScale=0.1
        if VScale1 >= 5120 and VScale1 <= 5121:
            self.VScale=0.05
        
        if self.Acquiris == True:
           BitSize = self.VScale/256.0
           self.Timetrace = ((self.Timetrace/float(self.Shots))-128.0)*BitSize
        return self.Timetrace


Exptime_pts = int(round((DigRate*10**9) * Exptime))
print Exptime_pts

fname0 = os.path.abspath('E:\MMW\Pchemlab\OCS_J2221_10mT_referenceNutation_10kavg_500mV_neon_2.trc')

#outname = str(fname0[(fname0.find('Pchemlab')+8):-4]+'_Curve.txt')
#path_to_outfile=os.path.abspath("E:\\MMW\\Pchemlab\\" + outname)


Trace1 = ScopeTrace()
FIDtrace0 = Trace1.openit(fname0)
FIDtrace0 = Trace1.bin_to_voltage(Shots)


for j in range(ExpNum):
    f = 'OCS_J2221_10mT_referenceNutation_10kavg_500mV_test_neon_exp%i.txt' %j
    path_to_outfile=os.path.abspath("E:\\MMW\\Pchemlab\\" + f)
    f=open(path_to_outfile,'a')
    if j == 0:
        for i in range(Exptime_pts-200):
            f.write(str(FIDtrace0[i + j*Exptime_pts -200]) + '\n')
        f.close()
    else:
        for i in range(Exptime_pts):
            f.write(str(FIDtrace0[i + j*Exptime_pts- 200]) + '\n')
        f.close()

