#Write a python program to reverse the columns of a 2D array (mXn) using numpy.
import numpy as np
row = int(input())
col = int(input())
rows = []
print("[",end="")
for i in range(row):
    print(np.flip(np.array(input().split())),end="")
    if i != row - 1:
        print()
print("]")
    
