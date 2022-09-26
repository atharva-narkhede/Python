def series(n):
    if n <= 1:
        return n**5
    else:
        return n**5 + series(n-1)


num = int(input("Enter n value: "))

print("The sum of series is", series(num))
