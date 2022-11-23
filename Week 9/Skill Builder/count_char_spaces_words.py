#Write a program that will count the number of characters, spaces, words, and lines in a file. Words are separated by a white space character.

file=open("input.txt","r")
text = file.read()
space=dig=alph=charc =words= 0
lines=0
for i in text:
    if (i == " "):
        space += 1
    elif (i.isalpha()):
        alph +=1
    else:
        charc +=1
        
file.seek(0, 0)
for line in file:
     lines = lines+1
     
file.seek(0, 0)

for line in file:
    wordslist = line.split()
    words = words + len(wordslist)
    
print("Alphabets : {}\nSpaces : {}\nWords : {}\nLines : {}".format(alph, space, words, lines))
