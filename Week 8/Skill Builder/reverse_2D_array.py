#Write a python program to reverse the rows of a 2D array (mXn) using numpy.

import numpy as np

#User input

m = int(input()) 
n=int(input())

list_array=[]

for i in range(0,m):
    lst= input().split() 
    list_array.append(lst)

arr = np.array(list_array) 
print(arr[::-1])
