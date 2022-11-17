#A string S is passed as the input. The program must print the number of articles in S.
#The string S passed as the input need not be correct grammatically.
import string
input_string = input().strip()
count = 0
for char in string.punctuation:
    if char in input_string:
        input_string = input_string.replace(char," ")
words = [word for word in input_string.split()]    
for word in words:
    if word == 'an' or word == 'a' or word == 'the':
        count = count + 1
print(count)
