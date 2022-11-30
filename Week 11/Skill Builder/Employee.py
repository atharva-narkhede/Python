#A company maintains a database that has the details of all the employees. 
#There are two levels of employees where Level 1 is the top management having salary more than 10000 and Level 2 is the staffs who are getting a salary less than 10000




class Employee:
    def __init__(self,id,salary):
        self.id = id
        self.salary = salary
    
    def display_emp(self):
        print(self.id)
        print(self.salary)

class EmpLevel(Employee):
    def find_empLevel(self):
        if self.salary > 10000:
            print('Level 1')
        else:
            print('Level 2')
            


inp = input().split()
id = int(inp[0])
salary = float(inp[1])

obj = EmpLevel(id,salary)
obj.display_emp()
obj.find_empLevel()