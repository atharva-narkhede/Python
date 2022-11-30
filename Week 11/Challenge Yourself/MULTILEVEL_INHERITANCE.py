#MULTILEVEL INHERITANCE 
#Create 3 classes Person, Staff, TemporaryStaff. Here Person class will be inherited by the Staff class and the Staff class will be again inherited by the TemporaryStaff class.


class Person:

    def __init__(self,name):
        
        self.name = name
    
    def display1(self):
        
        print('Person Name:{}'.format(self.name))
        
class Staff(Person):
    
    def __init__(self,name,staffid):
        
        super().__init__(name)
        self.staffid=staffid
    
    def display2(self):
        
        print('Staff id:{}'.format(self.staffid))
        
class Temporarystaff(Staff):
    
    def __init__(self,name,staffid,days,hours_worked):
        super().__init__(name,staffid)
        
        self.days=days
        self.hours_worked=hours_worked
        
        
    def display3(self):
        
        salary=self.days*self.hours_worked * 50
        print("Number of days:{}".format(self.days))
        print("Number of hours worked:{}".format(self.hours_worked))
        print("Total Salary:{}".format(salary))
        
        
name=input()
staffid=input()
days=int(input())
hours_worked=int(input())

obj=Temporarystaff(name, staffid, days,hours_worked)

obj.display1()
obj.display2()
obj.display3()