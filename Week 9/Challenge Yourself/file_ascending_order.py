#File Ascending Order 
#Consider a input file "numbers.txt" with integer values. Write a program to Open the file and sort the content of the file in ascending order.

file = open("numbers.txt", "r")
numbers = []

for line in file:
  numbers.append(int(line))

numbers.sort()
print(numbers)
file.close()
