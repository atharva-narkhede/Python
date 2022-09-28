n=int(input())
a=1
b=1
k=35
o=30
for i in range(1,n+1):
    if i%2==0:
        print(k," ",end="")
        k=k+(6*a)
        a+=1
    if i%2!=0:
        print(o," ",end="")
        o=o+(8*a)
        b+=1
    