
#Write a program to get the top three items in a shop using dictionaries.

# You are using Python
from heapq import nlargest
from operator import itemgetter
n = int(input())
items = {}
for i in range(n):
    dict1 = {}
    inp = input().split(':')
    items[inp[0]] = inp[1]
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)