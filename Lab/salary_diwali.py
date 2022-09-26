char=input("Enter sex of an employee(m or f): ")
salary=int(input("Enter salary of an employee: "))
if(char=='m' and salary<10000):
    bonus=(7*salary)/100
    salary=salary+bonus
elif(char=='m' and salary>=10000):
    bonus=(5*salary)/100
    salary=salary+bonus
elif(char=='f' and salary<10000):
    bonus=(12*salary)/100
    salary=salary+bonus
else:
    bonus=(10*salary)/100
    salary=salary+bonus
print("The salary is",salary)
