"""
Fair Francis

"Think Academy" has arranged for a competitive test for engineering students from rural villages. Those successful students of the test will be awarded the scholarship for their GRE/TOEFL preparations at Think Academy. Francis, the co-coordinator and founder of the academy has N different problem sets and there are N students who are appearing for the test. Each problem set contains zero or more problems. He will give each student exactly one problem set. But the problem sets might contain a different number of problems in each one, which looks unfair.

Since Francis is a fair tutor, he decided to move some problems from the problem set to another problem set (he can do this multiple times), until all problem sets contain the same number of problems.

Sometimes it's impossible to do so, and he might need to delete some problems completely before moving any problem, then he will start moving the problems. He needs your help to write a program to calculate the minimum number of problems to be deleted, and the minimum number of problems to be moved.
"""

n = int(input())
arr = [int(i) for i in input().split()][:n]
count = 0
avg = sum(arr)//n
for i in range(0,n):
    if avg>arr[i]:
        count+=avg-arr[i]
rem =sum(arr)-(avg*n)
print(rem,count)