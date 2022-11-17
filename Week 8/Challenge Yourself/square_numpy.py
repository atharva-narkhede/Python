#Write a python program to compute the determinant of a square array using Numpy function.
import numpy as np
n = int(input())
m_list = []
for i in range(n):
    inp = [int(i) for i in input().split()]
    m_list.append(inp)
twod_array = np.array(m_list)
det = np.linalg.det(twod_array)
print(det)
