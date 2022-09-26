def table(n):
    for i in range(1, 11):
        print(n, "*", i, "=", n*i)


for i in range(1, 11):
    print("Table of", i)
    table(i)
    print("")
