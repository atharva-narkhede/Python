#Write a python program to get the indices of the sorted elements of a given array using Numpy function.


import numpy as np
a=input().split()
arr=np.array(a,int)
i =np.argsort(arr)
print(i)
