#Recreation Fair - The Warner's Club arranged for a Recreation Fair for kids and adults for the winter season ahead. The Club offered outdoor activities for adults like hiking, cycling, power soccer and indoor activities like chess, carom and card games for kids below 10 years. Gary and Dory accompanied their parents for the fair and wanted to play the cricket collectible card game as they are crazy about the collectible cards.
# You are using Python
import math
def hcf(a,b):
    if(a<b):
        smaller = a
    else:
        smaller = b
    for i in range(1, smaller+1):
        if(a%i==0 and b%i==0):
            hcf = i
    return hcf
a = int(input())
b = int(input())
print(hcf(a,b))
