#Write a program to obtain the radius of the circle as a parameter and use three different functions to find the diameter, circumference, and area of the circle. Each function should return the respective values. Input format The input consists of the radius of the circle. Output format The output prints the diameter, circumference, and diameter. Round off the output to two decimal places. Refer sample input and output.



def diameter(r):
    return 2*r
       
def circle(r):
    return 2*3.14*r
    
def area(r):
    return 3.14*(r**2)
    
r=float(input())

print("Diameter of a circle = ",end="")
print("{:.2f}".format(diameter(r)))
print("Circumference of a circle = ",end="") 
print("{:.2f}".format(circle(r)))
print("Area of a circle = ",end="")
print("{:.2f}".format(area(r)))