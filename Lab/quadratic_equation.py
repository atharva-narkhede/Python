import math
a=int(input("Enter coefficient of x^2: "))
b=int(input("Enter coefficient of x: "))
c=int(input("Enter constant value: "))
d=(b**2)-(4*a*c)

if(d==0):
    x=(-b/2*a)
    print("Only one real root exist: ",x)
elif(d>0):
    x=(-b+(d)**0.5)/2*a
    y=(-b-(d)**0.5)/2*a
    print("Two real roots exist ",x,y)
elif(d<0):
    x=(-b+(d)**0.5)/2*a
    y=(-b-(d)**0.5)/2*a
    print("Two imaginary roots exist ",x,y)
else:
    print("!! Invalid !!")
