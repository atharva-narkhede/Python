#Hierarchical Inheritance:
#Create a class 'Parent'. 'Parent' class should have a method 'add' which prints the addition of 2 integers.
#Create a class 'child1' which should be a 'child' class of 'parent' class.it has a method 'sub' which prints subtraction of 2 integers.
#Create a class 'child2' which should be a child class of 'Parent' class. 'Child2' class should have a method 'mul' which prints multiplication of 2 integers.
#Create an object for a 'Child1' class. Call the 2 methods to add and sub from the child1 class object and display the result.
#Create an object for a 'Child2' class. Call the method mul from the child2 class object and display the result.


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


a=int(input()) 
b=int(input()) 
obj=child1(a,b)
obj.add()
obj.sub()
obj2=child2(a,b)
obj2.mul()