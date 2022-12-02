#You are given 2 values a , b and Number of test cases T. Perform Integer division and print the value of a // b. In the case of ZeroDivisionError or ValueError, print the error code.


t = int(input())
for _ in range(t):
    a, b = input().split()
    try:
        div = int(a) // int(b)
        print(div)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
