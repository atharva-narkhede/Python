#Create a multilevel inheritance based on the image given below. Create suitable attributes and methods as shown in the below table. Get the details from the user and display the data with the total bill amount.
#Create an object only from 'Bill' clause and display all the patient details (check output format) along with the calculated Bill amount.


class Patient:
    def __init__(self, patient_id, patient_name, age, gender):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.age = age
        self.gender = gender

    def displayData1(self):
        print(self.patient_id)
        print(self.patient_name)
        print(self.age)
        print(self.gender)

class In_Patient(Patient):
    def __init__(self, patient_id, patient_name, age, gender,room_number, consultation_fee, test_fee, number_days,rent_per_day):
        super(). __init__(patient_id, patient_name, age, gender)
        self.room_number = room_number
        self.consultation_fee = consultation_fee
        self.test_fee = test_fee
        self.number_days = number_days
        self.rent_per_day = rent_per_day

    def displayData2(self):
        print(self.room_number)
        print(self.consultation_fee)
        print(self.test_fee)
        print(self.number_days)
        print(self.rent_per_day)

class Bill(In_Patient):

    def __init__(self, patient_id,patient_name,age, room_number,gender, consultation_fee, test_fee, number_days, rent_per_day):
        super().__init__(patient_id,patient_name,age, room_number,gender, consultation_fee, test_fee, number_days, rent_per_day)


    def total_bill_amount(self):
        tot_amt = self.consultation_fee + self.test_fee + (number_days * rent_per_day)
        print(tot_amt)


#Main Program
patient_id = input()
patient_name = input()
age = input()
gender = input()
room_number = input()
consultation_fee = float(input())
test_fee = float(input())
number_days = int(input())
rent_per_day = float(input())

obj = Bill(patient_id,patient_name,age,gender, room_number, consultation_fee, test_fee, number_days, rent_per_day)
obj. displayData1()
obj. displayData2()
obj. total_bill_amount()
