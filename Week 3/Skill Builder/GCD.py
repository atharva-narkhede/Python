#Given 2 integers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1

N=int(input())
M=int(input())
i=1
hcf=0
k=-1
if N==0 and M!=0:
    print(M)
elif M==0 and N!=0:
    print(N)
else:
    while(i<=N and i<=M):
        if(N%i==0 and M%i==0):
            hcf=i
        i+=1
    if hcf>0:
        print(hcf)
    else:
        print(k)
