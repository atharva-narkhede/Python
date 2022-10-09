#The Event Organizing Company "Buzzcraft" focuses on event management to create a win-win situation for all involved stakeholders. Buzzcraft doesn't look at building one-time associations with clients, instead, aim at creating long-lasting collaborations that will span years to come. This goal of the company has helped them evolve and gain more clients within a notable time.

count=int(input())  
n=0
i=1
while n<count:
  j=1
  ct=0
  while j<=i:
    if i%j==0:
      ct=ct+1
    j=j+1
  if(ct==2):
    print(i,end=" ")
    n=n+1
  i=i+1
