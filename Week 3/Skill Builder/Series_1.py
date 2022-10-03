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