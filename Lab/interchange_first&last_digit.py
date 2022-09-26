num = int(input("Enter a number: "))
rev = 0
count = 0
temp = num
while temp > 0:
    temp = int(temp/10)
    count = count+1
if count < 2:
    print("\nIt is a Single digit Number!")
else:
    temp = num
    while temp > 0:
        rem = temp % 10
        rev = (rev*10)+rem
        temp = int(temp/10)
    revnum = rev
    rev = 0
    temp = num
    countTemp = count
    while temp > 0:
        remTemp = revnum % 10
        if countTemp == count:
            rem = temp % 10
            rev = (rev*10)+rem
        elif countTemp == 1:
            rem = temp % 10
            rev = (rev*10)+rem
        else:
            rev = (rev*10)+remTemp
        temp = int(temp/10)
        revnum = int(revnum/10)
        countTemp = countTemp-1
    print("\nNew Number: ")
    print(rev)
