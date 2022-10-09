# You are using Python
n,k = map(int,input().split())

lst = list(map(int,input().split()))
# print(lst)
sum = 0
for i in lst:
    sum += i//k
print(sum)