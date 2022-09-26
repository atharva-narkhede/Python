def palindrome(temp):
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = (rev*10)+rem
        temp = int(temp/10)
    return rev


n = int(input("Enter a number: "))
if (palindrome(n) == n):
    print("Palindrome")
else:
    print("Not a Palindrome")
