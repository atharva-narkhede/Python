#Accept a file name from the user and perform the following operations 
#1) Print the last line of the file in upper case 
#2) Print the number of words and number of characters in the file 
#3) Write the maximum times occurring word in the file with its count.

fin = open(filename, 'r')
lines = fin.read()  
lines_lst = lines.rstrip().split('\n')
print(lines_lst[-1].upper())  
print(len(lines.split()), len(lines))  

maxct = 0
maxwrd = ''
lst = lines.split()
for wrd in lst:
    if lst.count(wrd) > maxct:
        maxct = lst.count(wrd)
        maxwrd = wrd
print(maxwrd, maxct)
