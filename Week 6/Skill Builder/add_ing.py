#Write a program to add 'ing' at the end of a given string (length should be at least 3).
string = input()
if string.endswith('ing'):
    print(string + "ly")
else:
    print(string + "ing")
