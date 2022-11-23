#Write a python program to find the index of nth repetition of an item k in an array using numpy function.

import numpy as np

a=input().split()
k=int(input())
n=int(input())

arr=np.array(a,int)

print(np.where(arr==k)[0][n-1])
