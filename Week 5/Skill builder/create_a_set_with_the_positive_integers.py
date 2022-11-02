#Write a Python program to create a set with the positive integers and arrange the numbers in ascending order.

# You are using Python
input_list = input().split()
for i in range(0,len(input_list)):
    input_list[i] = int(input_list[i])
S1 = set(input_list)
x = sorted(S1)
print(x)