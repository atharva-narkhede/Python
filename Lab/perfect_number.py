def perfect(n):
    sum = 0
    for i in range(1, n):
        if (n % i == 0):
            sum += i
    return sum


num = int(input("Enter a number: "))
if perfect(num) == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
