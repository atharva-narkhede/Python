#Write a program that has a list of numbers both positive as well as negatives. Create a new tuple that stores only the positive values from the list

numbers=tuple()
newtup=()
n=int(input())
for i in range(0,n):
    num=int(input())
    numbers=numbers+(num,)
print("The elements in the tuple are:",numbers)
for i in numbers:
    if i>0:
        newtup+=(i,)
print(newtup)
