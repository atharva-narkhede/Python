# You are using Python
def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a,b,c=input().split(',')
print(max(a,b,c))