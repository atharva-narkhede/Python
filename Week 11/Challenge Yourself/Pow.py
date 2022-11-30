#Write a program to create the following: 
#Class Name: Pow parameters: a, b (integers) 
#Method: display (to print the value of a to the power of b) 
#Class Name: Pow1 (child class of Pow) parameters: inherited from Pow 
#Method: display1 (to print the value of a*b)

class Power:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def display(self):
        print(self.a**self.b)
        
class Power1(Power):

    def display1(self):
        print(self.a*self.b)
        
x = int(input())
y =int(input())
obj=Power1(x,y)
obj.display()
obj.display1()
