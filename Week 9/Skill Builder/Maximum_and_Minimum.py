#Maximum and Minimum: Write a program to obtain an integer array and write them to a file named "input.txt". Find the maximum and minimum elements.


file = open("input.txt", "r")
numbers = []
for line in file:
    numbers.append(int(line))
print(max(numbers))
print(min(numbers))
    
