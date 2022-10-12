#Write a program that accepts n numbers from the user, stores them in a tuple, and prints the length, maximum and minimum number from the tuple.

numbers=tuple()
newtup=()
i=1
while(i):
    num=int(input())
    numbers=numbers+(num,)
    i=int(input())
    
print("The elements in the tuple are:",numbers)
print("The length of the tuple :",len(numbers))
print("The Maximum number is :",max(numbers))
print("The Minimum number is :",min(numbers))