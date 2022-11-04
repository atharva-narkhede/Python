#Create a dictionary for a stationery shop (Pen, Pencil, Paper, etc…) and print all unique values in a dictionary.

n= int(input())
stat = []
for i in range(n):
    dict1 = {}
    inp = input().split(':')
    dict1[inp[0]] = inp[1]
    stat.append(dict1)
u_value = set(val for dict1 in stat for val in dict1.values())
print(sorted((set(u_value))))
