#Write a program that accepts a string S, and characters c1, c2. Replace character c1 with c2 and c2 with c1 using map() function. Input : S =”callege” c1 = ‘a’, c2 = ‘o ‘ Output : ‘college’

# You are using Python
def replace(s, c1, c2):
    l=len(s)
    
    for i in range(l):
        if s[i]==c1:
            s=s[0:i]+c2+s[i+1:]
            
        elif s[i]==c2:
            s=s[0:i]+c1+s[i+1:]
            
    return s
    
s=str(input())
c1=str(input())
c2=str(input())
print(replace(s,c1,c2))