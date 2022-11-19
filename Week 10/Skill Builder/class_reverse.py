#Create a class called Reverse. Write a Python program to reverse a string

class Reverse:
    def string_reverse(str1):
        rstr1 = ''
        index = len(str1)
        while index > 0:
            rstr1 += str1[ index - 1 ]
            index = index - 1
        return rstr1
str1=input()
print(Reverse.string_reverse(str1))
