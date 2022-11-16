#Write a python program to get the common unique items between two arrays sorted in ascending order using numpy function.
import numpy as np
arr1 = np.array(list(map(int,input().split())))
arr2 = np.array(list(map(int,input().split())))
arr1 = np.unique(arr1)
arr2 = np.unique(arr2)
common_arr = np.intersect1d(arr1,arr2)
print(np.sort(common_arr))
