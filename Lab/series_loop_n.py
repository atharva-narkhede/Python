n = int(input("Enter value of n:"))
sum = 0
for i in range(1, n):
    term = 1/(i+1)
    print("1/", (i+1), sep="")
    sum += term
print("Sum = ", sum)
