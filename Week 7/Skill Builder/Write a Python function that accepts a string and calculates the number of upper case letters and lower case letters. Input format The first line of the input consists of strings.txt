
#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters. Input format The first line of the input consists of strings. Output format Output prints the number of upper case and lower case.





# You are using Python
def string_test(s):
    lower=0
    upper=0
    for c in s:
        if c.isupper():
            upper+=1
        elif c.islower():
            lower+=1
        else:
            pass
    print(upper)
    print(lower)
    
s=input()
string_test(s)