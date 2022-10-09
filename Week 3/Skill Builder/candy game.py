#Candy Game Mona set off with great zeal to the "Fun Fair 2017". There were numerous activities in the fair, though Mona liked the Candy game. Delicious candies were wrapped in colorful foiled sheets with some random numbers on each of the candies.
n=int(input())
c=0
while n>0:
    if n%10==4:
        c+=1
    n=n//10
print(c)

#The code below also works the same question
#num = input()
#num = list(num)
#print(num.count("4"))
