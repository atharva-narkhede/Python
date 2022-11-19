#Create methods for the Calculator class that can do the following:
#Add two numbers.
#Subtract two numbers.
#Multiply two numbers.
#Divide two numbers.

class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    

a = int(input())
b = int(input())

obj = Calculator(a,b)
choice = int(input())
if choice == 1:
    print(obj.add())
elif choice == 2:
    print(obj.sub())
elif choice == 3:
    print(obj.mul())
elif choice == 4:
    print(obj.div())
else:
    print("Invalid choice")
