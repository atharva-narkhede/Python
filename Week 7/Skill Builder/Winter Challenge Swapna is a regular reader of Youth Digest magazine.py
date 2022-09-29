#Winter Challenge 
#Swapna is a regular reader of Youth Digest magazine. The magazine has a whole host of fun and interesting facts from around for the youth especially that encourage interactivity and enhances their imagination. "Winter Challenge" is an event announced in the December month edition of the magazine. Readers of the magazine who are between 10 to 15 years can participate in the special challenge. Those readers who participate and give the correct answer for the challenge will avail exciting gift coupons. According to the event, the challenge published was: Given 0 < x < m, where x and m are integers, the modular inverse of x is the unique integer n, 0 < n < m, such that the remainder upon dividing x × n by m is 1. For example, 4 x 13 = 52 = 17 x 3 + 1, so the remainder when 52 is divided by 17 is 1, and thus 13 is the inverse of 4 modulo 17. Swapna wants your help to find the correct answer for the problem based on the inputs given in the magazine. You are to write a program which accepts as input the two integer#s x and m, and outputs either the modular inverse n, or -1 if there is no such integer n. You may assume that m ≤ 100.


def findValue(n1,n2):
    s=0
    for i in range(0,1000000):
        if((n2*i+1)%n1 == 0):
            s=1
            return ((n2*i+1)//n1)
    if s==0:
        return -1
n1=int(input())
n2=int(input())
print(findValue(n1,n2))