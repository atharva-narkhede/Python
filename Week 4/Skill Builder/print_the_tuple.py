#Write a program to create a list of tuples with the first element as the number and the second element as the square of the number.

l_range=int(input())
u_range=int(input())
a=[(x,x**2) for x in range(l_range,u_range+1)]
print(a)