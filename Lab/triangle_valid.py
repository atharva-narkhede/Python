a=int(input("Enter 1st angle "))
b=int(input("Enter 2nd angle "))
c=int(input("Enter 3rd angle "))
s=a+b+c
if(s==180 and a!=0 and b!=0 and c!=0):
    print("Triangle is valid")
else:
    print("!!! Invalid Triangle !!!")
