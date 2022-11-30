#METHOD OVERLOADING
#Create a class named Compute.
#Create a method area. Method area should print the area.
#Create an object obj1


class Compute:
 
    def area(self, x=None, y=None):
        
        if x!=None and y!=None:
            print(x*y)
        
        elif x!=None:
            print(x*x)
        
        else:
            print(0) 



input1 = int(input())
input2 = int(input())



obj1 = Compute()

obj1.area()
obj1.area(input1)
obj1.area(input1,input2)