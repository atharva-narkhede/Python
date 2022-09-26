#Write a Python function to reverse words in a string. Call the function in the main program along with the given input to get the output. 

#Input format 
#Input consist of a sentence. 

#Output format 
#Output displays the reversed words in string.


def reverse_word(s):
    return ' '.join(reversed(s.split()))
    
s=input()
print(reverse_word(s))