# You are using Python
n=int(input())
sp=n
st=-1
for i in range(1,n+1):
    sp=sp-1
    st=st+2
    for j in range(1,sp+1):
        print("b",end="")
    for k in range(1,st+1):
        if(i>1 and i<n):
            if(k>1 and k<st):
                print("i")
            else:
                print("*",end="")
        else:
            print("*")
    for l in range(1,sp+1):
        print("b",end="")