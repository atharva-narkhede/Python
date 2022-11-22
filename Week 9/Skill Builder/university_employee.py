#A university posts its employee salary at salary.txt. Each line in the file consists of faculty first name, last name, designation and salary. 
#The columns are separated by a space. 
#Write a program to display the total salary and the average salary for assistant professors, associate professors, professors respectively. 
#Some sample lines in the file is shown below. 
#Deepak Sharma Professor 125000 
#Hemant Kumar Assistantprofessor 54000.78 
#Sushma Dinesh Associateprofessor 87000.50


file_txt = open("salary.txt")
pays = {}
for line in file_txt:
    *name, rank, pay = line.split()
    pays[rank] = pays.get(rank, []) + [float(pay)]
output_list = []
for rank, sals in pays.items():
    avg = sum(sals) / len(sals)
    fac = []
    fac.append(rank.title())
    fac.append(sum(sals))
    fac.append(avg)
    output_list.append(fac)

output_list.sort()
for fac in output_list:
    print(*fac)
file_txt.close()
