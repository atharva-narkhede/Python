num = int(input("Enter a number: "))
sum = 0
temp = a = num
count = 0
while (a > 0):
    count += 1
    a = a//10
if (count < 2):
    print("Single Digit number")
else:
    rev = 0
    while (temp > 0):
        rem = temp % 10
        rev = (rev*10)+rem
        temp = temp//10
print(rev)
