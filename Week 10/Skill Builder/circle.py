#Write a program with class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
#Class Name: Circle
#Method1: area
#Method2: perimeter
#Create an object for the class Circle and display the area and perimeter of a circle.
#Note: Use pi = 3.14

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

radius = int(input())
NewCircle = Circle(radius)
print(NewCircle.area())
print(NewCircle.perimeter())
