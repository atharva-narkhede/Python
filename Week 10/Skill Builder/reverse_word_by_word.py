#Write a program to reverse a string word by word. Use Python class to achieve the result.

class python_string:
    
    def __init__(self,inp_string):
        self.s = inp_string
        
    def reverse_words(self):
        
        return ' '.join(reversed(s.split()))



s= input()
#object
reverse = python_string(s)
print(reverse.reverse_words())
