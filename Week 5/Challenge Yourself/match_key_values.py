#Write a Python program to match key values in two dictionaries.

#Input : {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2} 

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y'%(key,value))