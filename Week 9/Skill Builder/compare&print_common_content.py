#Write a program to compare two files and print the common contents in them.


file_1 = open('input1.txt', 'r')
file_2 = open('input2.txt', 'r')

file_1_line = file_1.readline()
file_2_line = file_2.readline()


line_no = 1

print()

with open('input1.txt') as file1:
    with open('input2.txt') as file2:
        same = set(file1).intersection(file2)
same = sorted(same)
for line in same:
    print(line, end='')
