#Write a function called display() to display the following details.
#name (Datatype should be string)
#deposit amount (Datatype should be float)
#cost per day (Datatype should be float)


def display(name,depAmt,cost):
    print(name)
    print(depAmt)
    print(cost)

try:
    name = input()
    deposit = float(input())
    cost = float(input())
    display(name,deposit,cost)

except ValueError as ve:
    print('Invalid Input format')
