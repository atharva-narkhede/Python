#Write a Python program to generate a set in a set of lists whose sum of elements is the highest

list1 = []
list2 = []
list3 = []
list4 = []
list1 = input().split()
list2 = input().split()
list3 = input().split()
list4 = input().split()
for i in range (0,len(list1)):
    list1[i] = int(list1[i])
for i in range (0,len(list2)):
    list2[i] = int(list2[i])
for i in range (0,len(list3)):
    list3[i] = int(list3[i])
for i in range (0,len(list4)):
    list4[i] = int(list4[i])
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
set4 = set(list4)
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for num in list1:
    sum1 = sum1+num
for num in list2:
    sum2 = sum2+num
for num in list3:
    sum3 = sum3+num
for num in list4:
    sum4 = sum4+num
maximum = max(sum1,sum2,sum3,sum4)
print(maximum)
if sum1 == maximum:
    print(sorted(set1))
if sum2 == maximum:
    print(sorted(set2))
if sum3 == maximum:
    print(sorted(set3))
if sum4 == maximum:
    print(sorted(set4))
