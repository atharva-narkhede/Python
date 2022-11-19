#Write a Python class named Rectangle constructed by length and breath. Two methods which will compute the area and the perimeter of a Rectangle.
#Class Name: Rectangle
#Method1: area
#Method2: perimeter


class Rectangle():
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def area(self):
        print(self.a*self.b)
    
    def perimeter(self):
        print(2*(self.a + self.b))
    
a=int(input())
b=int(input())

obj=Rectangle(a,b)
obj.area()
obj.perimeter()
