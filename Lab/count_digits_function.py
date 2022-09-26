def digits(n):

    a = n//10
    if a == 0:
        return 1
    return 1 + digits(a)


num = int(input("Enter number: "))
print('Number of Digits: ', digits(num))
