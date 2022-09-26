total = 0
while True:
    num = int(input("Enter a number:"))
    if (num == 0):
        break
    else:
        total += num
print("Sum of numbers entered by user = ", total)
