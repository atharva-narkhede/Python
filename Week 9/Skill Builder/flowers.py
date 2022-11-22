#Assume a text file contains a flower name in each row. Read the contents of the file and display the flower names in sorted order (ascending)


file = open("flowers.txt", "r")
flowers = []
for line in file:
    flowers.append(line.rstrip('\n'))
flowers.sort()
file.close()
for ele in flowers:
    print(ele)
