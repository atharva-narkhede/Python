#Write a python script to find the reciprocal of the given list values and if there is any exception throw that to the user. 
#The given list is a Random list.


import sys
n = int(input())
randomList = []
for i in range(0,n):
    ele = input()
    randomList.append(ele)


for entry in randomList:
    try:
        r = 1/int(entry)
        print("The reciprocal of", entry, "is", r)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
