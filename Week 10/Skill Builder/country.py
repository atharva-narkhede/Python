#Create a class named Country with the following member variables/attributes.
#Get the inputs from the user and display as shown in the sample input and output.

class country:
    def prin(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        print("Country Name:",self.x)
        print("Country Code:",self.y)
        print("ISD Code:", self.z)

x=input()
y=input()
z=input()
r1=country()
r1.prin(x,y,z)
