#You are using a program to assist in the representative selection in your class. 
#Three persons are interested in contesting for the post. Each person is given a nomination id like ‘10’,’20’,’30’. 
#Every student in your class enters only the nomination id in the system.

inp_file = open("election.txt", "w")

nom_id = input()

while(nom_id != 'end'):
    inp_file.write(nom_id)
    inp_file.write("\n")
    nom_id = input()

inp_file = open("election.txt", "r")
contents = inp_file.readlines()

roll_10_count = contents.count("10\n")
roll_20_count = contents.count("20\n")
roll_30_count = contents.count("30\n")

inp_file = open("election.txt", "a")

inp_file.write("10 ")
inp_file.write(str(roll_10_count))
inp_file.write('\n')
inp_file.write("20 ")
inp_file.write(str(roll_20_count))
inp_file.write('\n')
inp_file.write("30 ")
inp_file.write(str(roll_30_count))

inp_file= open("election.txt","r")
for line in inp_file:
    print(line)
