#Write a program to replace the last element in a set with another set. Print the resultant set in sorted order




# You are using Python
input_list1 = input().split()
for i in range(0,len(input_list1)):
    input_list1[i] = int(input_list1[i])


input_list2 = input().split()
for i in range(0,len(input_list2)):
    input_list2[i] = int(input_list2[i])

S1 = set(input_list1)
S2 = set(input_list2)

S1 = set(input_list1[:-1])
S1.update(S2)
x = sorted(S1)
print(x)