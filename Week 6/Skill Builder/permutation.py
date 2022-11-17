#Write a program to find all permutations of a string.
def toString(List):
    return ''.join(List)

def permute(a,l,r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i] = a[i],a[l]
            
input_string = input()
n = len(input_string)
a = list(input_string)
permute(a,0,n-1)
