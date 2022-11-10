#X={”p‟,‟r‟,‟o‟,‟g‟,‟r‟,‟a‟,‟m‟,‟m‟,‟i‟,‟n‟,‟g‟, „i‟,‟n‟,‟ p‟,‟y‟,‟t‟,‟h‟,‟o‟,‟n‟} and Y={a,e,i,o,u} Using python sets X and Y, write scripts to find elements
#a) that occur only in X but not in Y
#b) that occur in X or Y.
#c) that occur in X and Y.
#d) Create a new set by deleting all vowels from X. 
#e) Check whether X contains all elements of Y, if so print “All vowels are in X”.

# You are using Python
X={"p","r","o","g","r","a","m","m","i","n","g","i","n","p","y","t","h","o","n"}
Y={"a","e","i","o","u"}

A=X.difference(Y)
a=list(A)
a.sort()

B=set()
B.update(X)
B.update(Y)
b=list(B)
b.sort()

C=set()
for i in X:
    for j in Y:
        if i==j:
            C.add(i)
c=list(C)
c.sort()

D=set()
D=X.difference(Y)
d=list(D)
d.sort()

print(a)
print(b)
print(c)
print(d)
if Y.issubset(X):
    print("All vowels are in X")
