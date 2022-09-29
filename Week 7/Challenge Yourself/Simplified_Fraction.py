from fractions import Fraction
def printValue(x,y):
    a=int(x/y)
    b=x%y
    if b==0:
        print(a)
    else:
        print(a,Fraction(b,y))
a=int(input())
b=int(input())
printValue(a,b)

