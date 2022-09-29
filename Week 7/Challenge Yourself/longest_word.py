#Write a program to define a function find_longest_word which accepts a list of words and returns the longest word in the list with its length. 


def find_longest_word(str):
    a=max(str.split(),key=len)
    return a
s=str(input())
w=find_longest_word(s)
print('Longest word:',w)
print('Length of the longest word:',len(w))