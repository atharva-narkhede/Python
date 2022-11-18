#Write a Python function that evaluates the mathematical functions f(x)=cos(2x), f′(x)=−2sin(2x), and f′′(x)=−4cos(2x) for given value of x.

from math import sin, cos, pi

def deriv2(x):
    return cos(2*x), -2*sin(2*x), -4*cos(2*x)
x=float(input())
f, df, d2f = deriv2(x)
print(f,df,d2f)
