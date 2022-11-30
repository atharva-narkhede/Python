#Hybrid Inheritance:
#Create a class 'Parent'. 'Parent' class should have a method 'add' which prints the addition of 2 integers.
#Create a class 'child1' which should be a 'child' class of 'parent' class.it has a method 'sub' which prints subtraction of 2 integers.
#Create a class 'child2' which should be a child class of 'Parent' class. 'Child2' class should have a method 'mul' which prints multiplication of 2 integers.
#Create a class 'child3' which should be a child class of 'child1' class and 'child2' class. 'Child3' class should have a method 'div' which prints the division of 2 integers.

class Parent:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

class child1(Parent):

    def sub(self):
        print(self.a - self.b)
        

class child2(Parent):

    def mul(self):
        print(self.a*self.b)
class child3(child1,child2):

    def div(self):
        print(self.a/self.b)

a=int(input()) 
b=int(input()) 
obj=child3(a,b)
obj.add()
obj.sub()
obj.mul()
obj.div()
