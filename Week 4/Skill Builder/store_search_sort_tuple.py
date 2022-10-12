#Write a program that accepts n numbers from the user, stores them in a tuple, searches for an element in the tuple, and sorts the tuple.

numbers=tuple()
newtup=()
n=int(input())
for i in range(0,n):
    num=int(input())
    numbers=numbers+(num,)
chk=int(input())
if chk in numbers:
    print("The element is present in the list")
else:
    print("The element is not present in the list")
print("The elements in the tuple are:",numbers)
print("The sorted elements of the tuple are:",sorted(numbers))
