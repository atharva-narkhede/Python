#Write a program that replaces text in a file. Your program should prompt the user to enter a filename, an old string, and a new string. 
#After replacing every occurrence of the string it should print the modified file contents on the screen. Here is a example. test.txt (filename)

filename = input()
old_string = input()
new_string = input()
inp_file = open(filename, "r")
out_file = open("result.txt", "w")
for line in inp_file:
    out_file.write(line.replace(old_string, new_string))
out_file = open("result.txt", "r")
for line in out_file:
    print(line)
inp_file.close()
out_file.close()
