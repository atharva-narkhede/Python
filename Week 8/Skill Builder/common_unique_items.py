#Write a python program to get the common unique items between two arrays sorted in ascending order using numpy function.

import numpy as np
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(np.intersect1d(a,b))
