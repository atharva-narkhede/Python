from heapq import nlargest
from operator import itemgetter
n=int(input())
items = {}

for i in range(n):
    name, value = input().split()
    items[name] = float(value)
for name, value in nlargest(1, items.items(), key=itemgetter(1)):
    print(name, float(value))
