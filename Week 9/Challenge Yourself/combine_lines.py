#Write a python program to combine each line from first file(input1.txt) and the corresponding line in second file(input2.txt). 
#Store the result in file output.txt



fh1 = open("input1.txt")
fh2 = open("input2.txt")
fh3 = open("output.txt","w")
for line1, line2 in zip(fh1, fh2):
    str=line1+line2
    fh3.write(str)
fh1.close()
fh2.close()
fh3.close()
