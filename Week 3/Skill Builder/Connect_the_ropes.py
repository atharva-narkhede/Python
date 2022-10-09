n,k=map(int,input().split())
L=list(map(int,input().split()))
rope=L[0]+L[1]-(2*k)
for i in range(2,n):
    rope+=L[i]-(2*k)
print(rope)