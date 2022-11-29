#Write a Python program to count the frequency of words in a file and display it in the console.

file=open("input.txt","r+")
wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in sorted(wordcount.items()):
    print (k, v)
