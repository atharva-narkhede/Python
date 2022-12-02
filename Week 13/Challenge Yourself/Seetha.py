#Seetha wants to understand the process of exception handling. 
#She wants to print the variable x which was not assigned any value. 
#But she needs to print the error message 'An exception occurred' instead of getting an error 'variable x not declared'.
#Help her in this process.


try:
    print(x)
except:
    print('An exception occurred')