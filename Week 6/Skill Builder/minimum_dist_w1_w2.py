#A string S is passed as the input. Two words W1 and W2, which are present in the string S are also passed as the input. The program must find the minimum distance D between W1 and W2 in S (in forward or reverse order) and print D as the output.


s=input().split()
w1=input().strip()
w2=input().strip()
mi=len(s)
for i in range(0,len(s)):
    if s[i]==w1:
        for j in range(0,len(s)):
            if s[j]==w2 and mi>abs(i-j) and i!=j:
                mi=abs(i-j)
print(mi)
