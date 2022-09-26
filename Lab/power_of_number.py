def power(n, p):
    if p == 0:
        return 1
    return n*power(n, p-1)


num = int(input("Enter number: "))
pow = int(input("Enter power: "))
print(power(num, pow))
