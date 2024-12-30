import numpy as np
import matplotlib.pyplot as plt
import pathlib
import re


path =pathlib.Path(__file__).parent.resolve()
path = str(path.as_posix())+"/"

def MPout(filename= "profile.mp"):

    path =pathlib.Path(__file__).parent.resolve()
    path = str(path.as_posix())+"/"
    File = open(path+filename, "r")


    array = []
    inner_array = []

    i = 0
    for line in File:

        li =list(re.split(r'[\s,]+|\n', line))
        if li[0]=="":
            # print(li)
            # print(li[1:5])
            li =li[1:5]
            li = np.array([float(i) for i in li])
            inner_array.append(li)
        
        else:
            #inner_array = np.array([float(i) for i in inner_array])
            inner_array = np.array(inner_array)
            # print(inner_array)
            
            array.append(inner_array)
            inner_array = []

    array = array[4:]
    array = np.array(array) 


    return array

array = MPout()

array = np.mean(array,axis=0)
print(array[:,3].shape)

x =np.arange(0,20)
print(x)

plt.plot(x,array[:,3])
plt.savefig(path+"Temp_profile.png")
