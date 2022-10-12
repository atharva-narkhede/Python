#Write a program to find the intersection of two lists.

num=int(input())
arr=[]
for i in range(0,num):
    n=int(input())
    arr.append(n)
arr1=[]
for i in range(0,num):
    n=input()
    arr1.append(int(n))
a=list()
for i in arr:
    if i in arr1:
        if i not in a:
            a.append(int(i))
#a=list(dict.fromkeys(a))
print(a)