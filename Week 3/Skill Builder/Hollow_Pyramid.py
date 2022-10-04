#Hollow Pyramid The much-awaited event in the entertainment industry every year is the "Screen Awards". This year the event is going to be organized on December 25 to honor the Artists for their professional excellence in Cinema. The Organizers of the event, J&R Events, decided to design some attractive and LED Matrix panel boards for the show promotions all across the venue.
# You are using Python
n=int(input())
sp=n
st=-1
for i in range(1,n+1):
    sp=sp-1
    st=st+2
    for j in range(1,sp+1):
        print("b",end="")
    for k in range(1,st+1):
        if(i>1 and i<n):
            if(k>1 and k<st):
                print("i")
            else:
                print("*",end="")
        else:
            print("*")
    for l in range(1,sp+1):
        print("b",end="")
