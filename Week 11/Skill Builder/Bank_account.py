#Bank Account
#A class that inherits another class obtains all the latter's attributes and methods are called inheritance. 
#The former is called Child class whilst the latter is called Parent class. 
#This phenomenon would be very promising in applications dealing with multiple classes that are constituted by similar or more likely the same attributes. 
#You will get to know the importance of inheritance from the following problem. 
#All types of accounts in a bank have common attributes which can be inherited from an Account class.

class Account:

    def __init__(self,accName,accNo,bankName):
        
        self.accName = accName
        self.accNo = accNo
        self.bankName = bankName
        

    def display(self):
        print('Account Holder Name:{}'.format(self.accName))
        print('Account Number:{}'.format(self.accNo))
        print('Bank Name:{}'.format(self.bankName))
        


class AdditionInfo1(Account):

    def __init__(self,tinNumber):
        self.tinNumber = tinNumber
        Account.__init__(self,accName_inp,accNo_inp,bankName_inp)
       

    def display(self):
        print('Account Holder Name:{}'.format(self.accName))
        print('Account Number:{}'.format(self.accNo))
        print('Bank Name:{}'.format(self.bankName))
        print('Tin Number:{}'.format(self.tinNumber))

class AdditionInfo2(Account):

    def __init__(self,orgName):
        self.orgName = orgName
        Account.__init__(self,accName_inp,accNo_inp,bankName_inp)
       

    def display(self):
        print('Account Holder Name:{}'.format(self.accName))
        print('Account Number:{}'.format(self.accNo))
        print('Bank Name:{}'.format(self.bankName))
        print('Organization Name:{}'.format(self.orgName))
        
        
        
        



accName_inp = input()
accNo_inp = input()
bankName_inp = input()
tinNumber = int(input())
orgName = input()


select = int(input())

if select == 1:
    accobj = Account(accName_inp,accNo_inp,bankName_inp)
    accobj.display()

if select == 2:
    accobj = AdditionInfo1(tinNumber)
    accobj.display()


if select == 3:    
    accobj = AdditionInfo2(orgName)
    accobj.display()