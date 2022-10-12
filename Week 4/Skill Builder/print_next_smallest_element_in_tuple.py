#You are given a list. For each element present in the list your task is to print the next smallest number than that number. If it is not the smallest print -1.

n=int(input())
arr= [int(i) for i in input().split()][:n]
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i]=arr[j]
            break
        if j==n-1:
            arr[i]=-1
arr[n-1]=-1
print(*arr)