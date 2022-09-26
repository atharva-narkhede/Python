b=int(input("Enter basic Salary: "))
if(b<=0):
    print('Invalid Input')    
    
elif(b>0 and b<=10000):
    hra=(b)*(20/100)
    da=(b)*(80/100)
    gross_salary=b+hra+da
    print("The Gross Salary is ",gross_salary)
elif(b<= 20000):
    hra=(b)*(25/100)
    da=(b)*(90/100)
    gross_salary=b+hra+da
    print("The Gross Salary is ",gross_salary)
elif(b> 20000):
    hra=(b)*(30/100)
    da=(b)*(95/100)
    gross_salary=b+hra+da
    print("The Gross Salary is ",gross_salary)  
else:
    print('')
    



