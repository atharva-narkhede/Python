# Operator Overloading
# Create a class named 'Power' that should perform the power operation of arguments from 2 objects.
# Create a method overloading for the ** operator, so that it should perform power operation.
# Create an object obj1 and obj2 for class Power (passing arguments a and b respectively)
# After creating objects obj1 and obj2, obj1 ** obj2 should display the output of ab value
# Refer sample input and sample output for formatting specification.

class Power:
    def __init__(self,x):
        self.x = x
    
    def __pow__(self,other):
        return self.x ** other.x


a = int(input())
b = int(input())
obj1 = Power(a)
obj2 = Power(b)
print(obj1**obj2)