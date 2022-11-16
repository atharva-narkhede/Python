#Write a program to print the abbreviation for a given sentence.
s=input()
s=s.split()
print("The abbreviation is")
for i in range(0,len(s)):
    s[i]=list(s[i])
    
    if ord(s[i][0]) in range(65,91):
        print(s[i][0],end="")
