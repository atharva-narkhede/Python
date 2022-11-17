# Write a program to find the missing letter given a list of increasing letters.
def missing_letter(lst):
    for a,b in zip(lst,lst[1:]):
        if ord(b) - ord(a) > 1:
            return chr(ord(a) + 1)
            
inp_list = input().split()
print(missing_letter(inp_list))
