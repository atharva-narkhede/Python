"""
Math Challenge 

In connection to the National Mathematics Day celebration, the Regional Mathematical Scholars Society had arranged for a Maths Challenge Event where high school students participated in large numbers. The first level of the challenge was an oral quiz, followed by a written test in the second round.

In the second round, the problem that the students had to answer goes like this:

For every positive number ‘n’ we define a function streak(n)=k as the smallest positive integer k such that n+k is not divisible by k+1.
"""


s = int(input())
n = int(input())
count = 0
num = 1
for i in range(1,n+1):
    for j in range(i,n+s):
        if (j%num==0):
            num+=1
        else:
            break
    if s==num-1:
        count+=1
    num=1
print(count)