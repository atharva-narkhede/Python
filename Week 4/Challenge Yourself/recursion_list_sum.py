#Write a python program of recursion list sum.

n= int(input())

num_list = []
for i in range(n):
    x=input()
    for i in x.split(): 
        num_list.append(int(i))



sum = 0 

for num in num_list:
    sum += num

print(sum)