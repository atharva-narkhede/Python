#Series 3 The Event Organizing Company "Buzzcraft" focuses on event management to create a win-win situation for all involved stakeholders. Buzzcraft doesn't look at building one-time associations with clients, instead, aim at creating long-lasting collaborations that will span years to come. This goal of the company has helped them evolve and expand big with organizing many events to date.

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
    
