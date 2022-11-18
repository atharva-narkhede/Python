#Write a program to extract all mail id’s from the given input string. User must get dynamic input.
#If the string does not contain any mail id's then display 'Mail id is not present' .

import re

my_str = str(input())
emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)
if emails:
    for mail in emails:
        print(mail)
else:
    print("Mail id is not present")
