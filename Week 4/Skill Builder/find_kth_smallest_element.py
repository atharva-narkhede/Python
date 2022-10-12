#Write a program to find the Kth smallest element in an unsorted list.

l1 = []
n = int(input())
k = int(input())
for i in range(0,n):
    element = int(input())
    l1.append(element)
l1.sort()
print(l1[k-1])