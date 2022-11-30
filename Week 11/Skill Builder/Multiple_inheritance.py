#Multiple Inheritance
#Create a class 'Parent'. 'Parent' class should have a method 'add' which prints the addition of 2 integers.
#Create a class 'parent2' which is another 'parent' class that should have a method 'sub' which prints subtraction of 2 integers.
#Create a class 'Child' which should be a child class of 'Parent' class and 'parent2' class. 'Child' class should have a method 'mul' which prints multiplication of 2 integers.
#Create an object for a 'Child' class. Call the 3 methods to add, sub and mul from child class object and display the result.


class Parent:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

class parent2:

    def sub(self):
        print(self.a - self.b)
        

class Child(Parent,parent2):

    def mul(self):
        print(self.a*self.b)

a = int(input())
b = int(input())

ob = Child(a,b)

ob.add()
ob.sub()
ob.mul()

