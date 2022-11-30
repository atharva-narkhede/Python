#Create a class 'Complex' to add two complex numbers. The complex number contains the real parts and the imaginary parts. 
#Create two objects c1 and c2. c1 passes the first complex number. c2 passes the second complex number. 
#Create a method overloading for the '+' operator, so that it should perform complex numbers addition. 
#After creating objects c1 and c2, c1+c2 should display the addition of 2 complex numbers.



class complex_num:
    def __init__(self):
        self.real = 0
        self.imag = 0
    def assign(self,rl,img):
        self.real = rl
        self.imag = img
    def __add__(self,obj):
        temp = complex_num()
        r = self.real + obj.real
        i = self.imag + obj.imag
        temp.assign(r,i)
        return temp
    def __mul__(self,obj):
        temp = complex_num()
        r = self.real*obj.real - self.imag*obj.imag
        i = self.real*obj.imag + self.imag*obj.real
        temp.assign(r,i)
        return temp
    def __pow__(self,num):
        temp = complex_num()
        temp.assign(1,0)       
        while num>0:
            temp *= self
            num -= 1
        return temp
    def __eq__(self,obj):
        if self.real == obj.real:
            if self.imag == obj.imag:
                return True
            else:
                return False
        else:
            return False
    def __str__(self):
        return str(self.real)+'+'+str(self.imag)+'j'
a=int(input())
b=int(input())
c=int(input())
d=int(input())
c1 = complex_num()
c1.assign(a,b)
c2 = complex_num()
c2.assign(c,d)

print('(',c1+c2,')',sep="")
