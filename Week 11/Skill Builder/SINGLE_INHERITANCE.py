#SINGLE INHERITANCE
#Create a class 'Parent'. 'Parent' class should have a method 'add' which prints the addition of 2 integers.
#Create a class 'Child' which should be a child class of 'Parent' class. 'Child' class should have a method 'sub' which prints subtraction of 2 integers.
#Create an object for a 'Child' class. Call the 2 methods add and sub from the child class object and display the result.



class Parent:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

class Child(Parent):

    def sub(self):
        print(self.a - self.b)


a = int(input())
b = int(input())

ob = Child(a,b)

ob.add()
ob.sub()
