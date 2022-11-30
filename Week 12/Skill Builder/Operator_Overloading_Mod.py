#Operator Overloading
#Create a class named 'Mod' that should perform the mod operation of arguments from 2 objects.
#Create a method overloading for % operator, so that it should perform the mod operation.
#Create an object obj1 and obj2 for class Mod (passing arguments a and b respectively)
#After creating objects obj1 and obj2, obj1 % obj2 should display the output.
#Refer sample input and sample output for formatting specification.


class Mod:
    def __init__(self,x):
        self.x = x
    
    def __mod__(self,other):
        return self.x % other.x


a = int(input())
b = int(input())
obj1 = Mod(a)
obj2 = Mod(b)
print(obj1 % obj2)