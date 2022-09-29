# You are using Python
N=int(input())
def findSum(N):
    sumn=0
    for i in range(0,N+1):
        sumn+=(2**i)
    return int(sumn)
print(findSum(N))