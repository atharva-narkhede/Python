#Write a python function program to calculate power of a number raised to other. E.g.- ab using recursion.


# You are using Python
def power(a,b):
    if b==0:
        return 1

    return a*power(a,b-1)
    
a=eval(input())
b=eval(input())
print(power(a,b))