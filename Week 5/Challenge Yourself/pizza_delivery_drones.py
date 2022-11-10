#The Company is launching a network of autonomous pizza delivery drones and wants you to create a flexible rewards system - Pizza Points. 
#The rules are simple: if a customer has made at least N orders(min_order) of at least Y(min_price) price, they get a FREE pizza!!!

# You are using Python
n=int(input())
d={}
for i in range(n):
    c=[i for i in input().split()]
    s=c[0]
    d[s]=[]
    for j in range(1,len(c)):
        d[s].append(int(c[j]))
minorder=int(input())
maxorder=int(input())
l=[]
for i in d:
    count=0
    for j in d[i]:
        if j>=maxorder:
            count+=1
    if count>=minorder:
        l.append(i)
l.sort()
for i in l:
    print(i,end=" ")
