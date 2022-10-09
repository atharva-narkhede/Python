#Charity Dinner 
#WeCanNGO Trust is organizing a charity dinner at St. John’s College. Since older students are both wiser and richer, the members of the trust decide that the price of each ticket will be based on how many years the students have been in the school. A first-year student will buy a PINK ticket, a second-year student will buy a GREEN ticket, a third-year student will buy a RED ticket, and a fourth-year student will buy an ORANGE ticket.Assume that all tickets are sold. Each color of the ticket is uniquely priced. Write a program to output all combinations of tickets that produce exactly the desired amount to be raised. The combinations may appear in a specific order. First ORANGE is considered, then RED, then GREEN, and finally PINK. Also, display the total number of combinations found and the smallest number of tickets to be printed to raise the desired amount so that printing cost is minimized.

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
