#Sum of the Integers in the file 
#Consider an input file "numbers.txt" with integer values. Write a program to open the file and read the content to find the sum of all values in the file.

file = open("numbers.txt", "r")
numbers = []

for line in file:
  numbers.append(int(line))

print(sum(numbers))
file.close()
