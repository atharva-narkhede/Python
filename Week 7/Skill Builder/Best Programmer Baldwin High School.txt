#Best Programmer 
#Baldwin High School's Best Programmer Contest is organized today and the contest hones the students coding skills by making them solve different challenges. Based on the speed and accuracy with which the students finish the challenges, the Event coordinators will rank the participants and reward them. The entry level challenge was just one problem which the students has to program for. The problem reads like: A positive integer, n, is said to be perfect if the sum of its proper divisors equals the number itself. (Proper divisors include 1 but not the number itself.) If this sum is less than n, the number is deficient, and if the sum is greater than n, the number is abundant. The Event coordinators wanted to prepare the answer key for all the problems given in the contest so as to evaluate the submissions of the participants. Write a program using functions that reads a positive integer, determines if the integer is perfect, abundant or deficient and outputs the number along with its classification.



def check_num(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
            
    if(sum==n):
        return 0
    elif sum<n:
        return 1
    else:
        return -1
n=eval(input())
if(check_num(n)==0):
    print("perfect number")
elif(check_num(n)==1):
    print("Deficient number")
else:
    print("Abundant number")