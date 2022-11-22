#Write a program to count frequency of characters in a given file


import collections

file = open('sample.txt', 'w')
s = input()

file.write(s)
file.close()
with open('sample.txt', 'r') as info:
    count = collections.Counter(info.read())

for i in sorted(count):
    print((i, count[i]), end=" ")


file = open('sample.txt', 'r')
data = file.read()

file.close()
