#Given N values, Write a program to find the sum of the N values. If the user input is less than N values, then print Index Error message.Use Exception handling.


count = int(input())
inp = input().split()
result = 0
exception = 'False'

for i in range(count):
    try:
        result = result + int(inp[i])
    except IndexError as e:
        print(e)
        exception = 'True'
        break

if exception != 'True':
    print(result)

