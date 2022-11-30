#Printing object using str()
#Create a class named 'Vector' to get the values of x and y coordinates.
#Create an object obj1 by passing 2 arguments x and y.
#print(obj1) should display the below output
#xi+yj

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return str(self.x)+'i+'+str(self.y)+'j'


x = int(input())
y = int(input())

obj1 = Vector(x,y)
print(obj1)
