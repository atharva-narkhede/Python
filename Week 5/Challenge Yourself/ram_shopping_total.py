#Ram did grocery shopping. He has a list of items along with the quantity he bought and price of each item. 
#Can you please help him to find the total amount he spent.

# You are using Python
a=int(input())
d={}
e={}
s=0
for i in range(a):
    c=input().split()
    d[c[0]]=float(c[1])
    e[c[0]]=float(c[2])
for j in dict.fromkeys(d):
    s+=d[j]*e[j]
print(s)
