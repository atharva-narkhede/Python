#Write a program to get the input as integer from the user. If the input is not a valid integer throw an exception error displaying
#'Invalid Integer'. If the given input is valid integer, display 'Valid Integer'


try:
    x = int(input())
    print('Valid Integer')
except ValueError:
    print('Invalid Integer')
