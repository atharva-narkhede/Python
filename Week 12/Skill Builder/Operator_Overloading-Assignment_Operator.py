# Operator Overloading - Assignment Operator +=
# Create a class named 'Assignment' that should perform += operation of arguments from 2 objects.
# Create a method overloading for += operator, so that it should perform an addition assignment operation.
# Create an object obj1 (passing arguments a and b)
# Create an object obj2 (passing arguments c and d)
# After creating objects obj1 and obj2, print(obj2 += obj1) should display the output as below

class Assignment:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __iadd__(self,other):
        self.a += other.a
        self.b += other.b
        return self.a,self.b
    
    
a = int(input())
b = int(input())
c = int(input())
d = int(input())

obj1 = Assignment(a,b)
obj2 = Assignment(c,d)
obj2 += obj1
print(obj2)

