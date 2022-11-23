#Write a program to extract all odd number from a numpy array using numpy module.

# You are using Python
import numpy as np

inp=input().split()

arr=np.array(inp,int)

print(arr[arr%2==1])
