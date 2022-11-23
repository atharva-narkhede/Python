#Write a NumPy program to create a nXn matrix and fill it with a checkerboard pattern.


# You are using Python
import numpy as np
n=int(input())
x=np.zeros((n,n),dtype=int)
x[1::2,::2]=1
x[::2,1::2]=1

print(x)
