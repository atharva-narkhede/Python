#Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

# You are using Python
n=int(input()) 
number_list = []
for i in range(n):
    number_list.append(int(input())) 
position =3-1
idx = 0 
len_list = len(number_list)
while len_list > 0: 
    idx = (position + idx)% len_list; 
    print(number_list.pop(idx)) 
    len_list-=1