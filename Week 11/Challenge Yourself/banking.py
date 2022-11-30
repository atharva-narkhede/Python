#Considering the Banking Scenario, You have different types of accounts like Current Account, Savings Account which inherits the base class Account. Create a base class Account with the fields - name, acc_number, principal_amount, and start_date. 
#Create two subclasses CurrentAccount & SavingsAccount for base class 'Account' Declare a method calculateInterest which would return the interest and get end_date as a parameter. 
#In SavingsAccount & CurrentAccount - The interest is calculated as simple interest(per year). (Interest 12% for the savings account and 5% for the Current account.)



import datetime

class Account:

    def __init__(self,name, acc_number, acc_type, principal_amount, start_date):
        self.name = name
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.principal_amount = principal_amount
        self.start_date = start_date

    def display_details(self):
        print(self.name)
        print(self.acc_number)
        print(self.acc_type)
        print(self.principal_amount)  
       


class SavingsAccount(Account):

    def __init__(self,name, acc_number, acc_type, principal_amount, start_date, end_date):
        super().__init__(name, acc_number, acc_type, principal_amount, start_date)
        self. end_date = end_date
        
    def calculateInterest(self):

        
        s_date_list = self.start_date.split('-')
        s_date_y = int(s_date_list[0])
        s_date_m = int(s_date_list[1])
        s_date_d = int(s_date_list[2])

        e_date_list = self.end_date.split('-')
        e_date_y = int(e_date_list[0])
        e_date_m = int(e_date_list[1])
        e_date_d = int(e_date_list[2])

        d1 = datetime.datetime(e_date_y, e_date_m, e_date_d)
        d2 = datetime.datetime(s_date_y, s_date_m, s_date_d)

        month_diff = d1.month - d2.month + 12*(d1.year - d2.year)
        
        interest = self.principal_amount * (12/100) * (month_diff/12)
        print(interest)

class CurrentAccount(Account):

    def __init__(self,name, acc_number, acc_type, principal_amount, start_date, end_date):
        super().__init__(name, acc_number, acc_type, principal_amount, start_date)
        self. end_date = end_date
        
    def calculateInterest(self):

        s_date_list = self.start_date.split('-')
        s_date_y = int(s_date_list[0])
        s_date_m = int(s_date_list[1])
        s_date_d = int(s_date_list[2])

        e_date_list = self.end_date.split('-')
        e_date_y = int(e_date_list[0])
        e_date_m = int(e_date_list[1])
        e_date_d = int(e_date_list[2])

        d1 = datetime.datetime(e_date_y, e_date_m, e_date_d)
        d2 = datetime.datetime(s_date_y, s_date_m, s_date_d)

        month_diff = d1.month - d2.month + 12*(d1.year - d2.year)
        interest = self.principal_amount * (5/100) * (month_diff/12)
        print(interest)
        

acc_name = input()
acc_number = input()
acc_type = input()
principal_amount = float(input())
start_date = input()
end_date = input()

if acc_type == 'Savings':
    obj = SavingsAccount(acc_name, acc_number, acc_type, principal_amount, start_date, end_date)
    obj. display_details()
    obj. calculateInterest()

elif acc_type == 'Current':
    obj = CurrentAccount(acc_name, acc_number, acc_type, principal_amount, start_date, end_date)
    obj. display_details()
    obj. calculateInterest()    

