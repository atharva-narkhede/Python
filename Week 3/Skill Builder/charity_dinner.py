p=int(input())
g=int(input())
r=int(input())
o=int(input())
t=int(input())
count = 0
c = t
for i in range(0,t+1):
    for j in range(0,t+1):
        for k in range(0,t+1):
            for l in range(0,t+1):
                if(p*i+g*j+r*k+o*l==t):
                    print("# of PINK is",i,"# of GREEN is",j,"# of RED is",k,"# of ORANGE is",l)
                    count+=1
                    if c>(i+j+k+l):
                        c=i+j+k+l
print("Total combinations is",count)
print("Minimum number of tickets to print is",c)
