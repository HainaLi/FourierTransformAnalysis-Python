# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:18:32 2014

@author: Nate
"""



import numpy as np


#array containing normal mode energies
E = np.array((151.05,170.05,393.3,429.4,475.95,558.6,583.3,648.85,730.55,739.1,774.25,782.8,816.05,910.1,997.5,1035.5,1047.85,1071.6,1072.55,1122.9,1156.15,1234.05,1240.7,1266.35,1396.5,1528.55,1582.7,1687.2,1716.65,2287.6,3192,3201.5,3212.9,3221.45,3226.2,3198.65)) #calculated (HF-6-31G*)


E_init = 1000 #beginning of cm-1 range
E_fin = 10000 #end of cm-1 range
i = 100 #iteration

states_v_temp_array = np.array(())

for e in range (E_init,E_fin+i,i):

    Emin = 0 #cm-1
    Emax = e   
    
    N = 14 #atoms
    
    k = 3*N - 6 #degrees of freedom
    
      
    
    A = np.zeros((k), dtype = int)
    
    summation = 0
    
    
    i = 0
    
    j = 0
    
    case1 = True
    case2 = False
    counter = 0
    
    
    states = np.append(A, summation)
    counter = counter + 1
    #print states
            
    while (j >= 0):
            
        if (case1 == True):
            summation = 0
            A[i] = A[i] + 1
            #print A
            
            for n in range (0, k):
                summation = summation + (A[n])*(E[n])
              
            #print summation
            
            
            if (summation < Emin):
                case1 = True
                case2 = False
            elif(Emin <= summation and summation <= Emax):
                #store the state
                final = np.append(A, summation)
                counter = counter + 1
                #print final
                states = np.vstack((states, final))
               
                case1 = True
                case2 = False
            elif(summation > Emax):
                if A[i]!=0:
                    A[i] = A[i] - 1
                case1 = False
                case2 = True
    
        if (case2 == True):
            
            if i < (k-1):
                i = i + 1
                case1 = True
                case2 = False
            elif i == (k-1):
                for n in range(i-1,-2,-1):
                    if (A[n] != 0):
                        j = n
                        break
                    if (n < 0):
                        j = n
                   
                A[j] = A[j]-1
                
                for n in range (j+1,k):
                    A[n] = 0
                               
                
                i = j + 1
                case1 = True
                case2 = False
    print "number of states: ", counter, " at Emax = ",Emax
    #print states
    
    if e == E_init:
        states_v_temp_array = ((Emax,counter))
    else:
        states_v_temp_array = np.vstack((states_v_temp_array,(Emax,counter)))
        
    print states_v_temp_array
    
    np.savetxt('phenylacetylene_10000.csv',states_v_temp_array,delimiter =',')
