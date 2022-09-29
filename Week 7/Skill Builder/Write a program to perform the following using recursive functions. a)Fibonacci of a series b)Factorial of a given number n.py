#Write a program to perform the following using recursive functions. 
#a)Fibonacci of a series b)Factorial of a given number n


# You are using Python
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)
    
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
    
n1=eval(input())
n2=eval(input())

if n1<0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")

    for i in range (1,n1+1):
        print(fib(i))
        
if n2<0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    print("The factorial of {} is {}".format(n2,fact(n2)))