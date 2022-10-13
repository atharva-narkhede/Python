#Write a Python program to remove an empty tuple(s) from a list of tuples. Given Tuple: L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

# You are using Python
L = [(),(),('',),('a', 'b'), ('a', 'b', 'c'),('d')] 
result_list = [] 
for element in L: 
    if type(element) == tuple and len(element) == 0:
        continue
    else:
        result_list.append(element)

L= result_list

print(L)