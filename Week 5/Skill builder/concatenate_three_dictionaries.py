#Write a program to concatenate three dictionaries to create a new one.


# You are using Python
n=int(input())
list1=[]
list2=[]
list3=[]
for i in range(n):
    dict1 = {}
    inp = input().split(':')
    dict1[inp[0]] = inp[1]
    list1.append(dict1)
for i in range(n):
    dict2 = {}
    inp = input().split(':')
    dict2[inp[0]] = inp[1]
    list2.append(dict2)
for i in range(n):
    dict3 = {}
    inp = input().split(':')
    dict3[inp[0]] = inp[1]
    list3.append(dict3)
for d in list2:
    list1.append(d)
for d in list3:
    list1.append(d)
print(list1)