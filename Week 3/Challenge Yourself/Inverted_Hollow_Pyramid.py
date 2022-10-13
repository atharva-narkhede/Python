#Inverted Hollow Pyramid 

#The much-awaited event in the entertainment industry every year is the "Screen Awards". This year the event is going to be organized on December 25 to honor the Artists for their professional excellence in Cinema. The Organizers of the event, J&R Events, decided to design some attractive and LED Matrix panel boards for the show promotions all across the venue.

#The event organizers wanted to program the display boards with some specific pattern using alphabets and special characters. Help them write a program to design the pattern of an inverted hollow pyramid in the matrix panel, given the number of lines of the pattern.

n = int(input())
nu = 2*n-1
nn = n
for i in range(1,n+1):
    for j in range(1,nu+1):
        if(i==1):
            print("*",end="")
        elif (j<i)or(j>nu-i+1):
            print("b",end="")
        elif (j==i) or (j==nu-i+1):
            print("*",end="")
        else:
            print("i",end="")
    print()