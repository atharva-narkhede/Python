#A string S is passed as the input. The program must print the number of articles in S.
#The string S passed as the input need not be correct grammatically.

s=input()
s=s.lower()
s=s.split()
for i in range(0,len(s)):
    s[i]="".join(e for e in s[i] if e.isalnum())
print(s.count("a")+s.count("an")+s.count("the"))
