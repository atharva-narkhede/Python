#Write a numpy program to get the floor, ceiling and truncated values of the elements of a numpy array.
import numpy as np
array = np.array([float(i) for i in input().split(" ")])
print(np.floor(array))
print(np.ceil(array))
print(np.trunc(array))
