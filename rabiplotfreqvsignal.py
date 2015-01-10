import matplotlib as plt
import numpy as np
import os


xvalues = np.arange(-5.76, 5.76+0.48, 0.48)


print len(xvalues)

yvalues = []
count = 0 
for file in os.listdir('E:\\chem 3821\\Nutrationdata\\fouriertransform\\FT\\'):
    print "count: ", count

    if file.endswith("decay" + str(count) + "_FT.txt"):

        path_to_file = os.path.abspath('E:\\chem 3821\\Nutrationdata\\fouriertransform\\FT\\' + file) 
        print "Processing ", file 
        f = np.loadtxt(path_to_file)

        
        #freq = f[:,0]
        intensity = f[:,1]
        #print freq
        
        i = np.argmax(intensity)
        #print freq[i], intensity[i]
        #xvalues.append(freq[i])
        yvalues.append(intensity[i])
        count = count + 1
        

plt.pyplot.scatter(xvalues,yvalues)
    
plt.pyplot.xlabel('Pulse Length (s)')
plt.pyplot.ylabel('Intensity')
plt.pylab.show();
        