#Generate OTP
input_integer = input()
seperate_odd = []
for i in range(len(input_integer)):
    if i % 2 != 0:
        seperate_odd.append(int(input_integer[i]))
square_num = ""
for i in seperate_odd:
    square_num += str(i**2)
print(square_num[:4])
