#Number Of Lines in the file 
#Write the program to open the file and read the content to count the number of lines.

file = open("input1.txt", "r")
count =0
for line in file:
    count =count+1

print(count)
file.close()
