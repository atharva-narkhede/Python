#Create a class name Employee with the instance attribute firstname and lastname.
#Form the email by joining the first and last name together with a "." in between, and follow it with '@company.com' at the end. Make sure everything is in lowercase.
#Examples:
#emp_1 = Employee("John", "Smith")
#emp_2.email ➞ "mary.sue@company.com"

class Employee:
     
    def _init_(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_names(self):
        return self.first_name + " " + self.last_name
   
    def email(self):
        return self.first_name.lower() + "." + self.last_name.lower() + "@company.com"

x=input()
y=input()
employee_1 = Employee()
employee_1._init_(x,y)
employee_1.email()
print(employee_1.email())
