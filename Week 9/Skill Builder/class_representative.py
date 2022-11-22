#The class representative has asked every student in the class to enter their rollno, name and cgpa in google word document. 
#The students have filled the information in single rows, but in random order in a file called student.txt. 
#The information has to be read , sorted based on rollno and then written in a new file ‘sortedstudent.txt’ . 
#If input text file contains rows of information separated by the character ‘~’ as shown below:


def my_sort(line):
    line_fields = line.strip().split('~')
    roll_no = line_fields[0]
    return roll_no


fp = open('student.txt')
contents = fp.readlines()
contents.sort(key=my_sort)
out_file = open("sortedstudent.txt", "w")
for line in contents:
    out_file.write(line)
out_file = open("sortedstudent.txt", "r")
for line in out_file:
    print(line)
fp.close()
