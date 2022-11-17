#Balls for Challenge
#The Circoloco Children Carnival is the City’s largest and successful event dedicated to children and families. 
#The main focus at the carnival is the workshop arena where kids can participate in engaging and educational activities.


s1=input()
s2=input()
for i in range(0,len(s1)):
    if(s1[i]==s2[i]):
        if(s1[i]=="W"):
            print("B",end="")
        else:
            print("W",end="")
    else:
        print("B",end="")
