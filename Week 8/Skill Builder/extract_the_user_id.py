#Write a Program to extract the user id, domain name and suffix from the following email addresses.

import re

emails=input()
pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
result=re.findall(pattern,emails,flags=re.I)
for i in result:
    print(*i)
