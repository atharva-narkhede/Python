#Write a program to obtain the cost for 'n' days of an item and n as input and calculate the cost per day for the item. 
In case, zero is given as input for n, an arithmetic exception is thrown, handle the exception and prompt the user accordingly with an error message 'Division by Zero'


c = float(input())
a = int(input())
try:
    d = c / a
    print(d)
except ZeroDivisionError as e:
    print('Division by Zero')

