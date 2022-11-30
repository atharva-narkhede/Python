#Write a class named Circle constructed by a radius and two methods that will compute the area and the perimeter of a circle (Use pi = 3.14).
#Class Name: Circle
#Method1: area
#Method2: perimeter



class Circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        print(self.r**2*3.14)
    
    def perimeter(self):
        print(2*self.r*3.14)
        
class Square(Circle):

	def getArea(self):
		print(r*r)
  
	def getPerimeter(self):
		print(4*r)
		
r=int(input())
obj=Square(r)
obj.area()
obj.perimeter()
obj.getArea()
obj.getPerimeter()
