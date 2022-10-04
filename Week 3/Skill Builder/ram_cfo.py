#Ram is the CFO of an MNC. He wants to order the employee salaries in ascending order so that he can do a salary hike based on the salary values of employees. He selects you to do the task of sorting the salaries. Sort the salaries in ascending order and pass on the information to Ram.
# You are using Python
a=int(input())
num=list(map(int, input().split()))
num.sort()
print(*num)
