#Write a program to remove duplicate numbers from a list.

n= int(input())
l1 = []
for i in range (0,n):
    ele = int(input())
    l1.append(ele)
l2 = []
for num in l1:
    if num not in l2:
        l2.append(num);
print(l2)