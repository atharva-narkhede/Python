#Write a program to obtain an integer from the user and generate the OTP using the below steps.
#1.separate digits which are in odd place index (index starts from 0)
#2.square those numbers
#3. Return the first 4 digits.


input_integer = input()
seperate_odd = []
for i in range(len(input_integer)):
    if i % 2 != 0:
        seperate_odd.append(int(input_integer[i]))
square_num = ""
for i in seperate_odd:
    square_num += str(i**2)
print(square_num[:4])
