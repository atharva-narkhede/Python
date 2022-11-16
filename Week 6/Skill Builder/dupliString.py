#Write a program that takes a string, and returns a new string with any duplicate consecutive letters removed.
string = input()
result_string = ""
for char in string:
    if char not in result_string:
        result_string += char 
print(result_string)
