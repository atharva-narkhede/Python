"""
Lucky Cards 

The Hatfield Game Fair is the premier event of its kind for adults interested in some intellectual and cognitive brain games. Exciting games were organized for kids between the ages group of 8 and 10. One such game was the "Lucky Cards", a simple two-player game, played with a deck of cards. The cards in the deck have these possible names: two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace. The cards labeled jack, queen, king, ace is collectively known as high cards.

The numerical equivalent of the high cards is as given below:

Jack – 11

Queen – 12

King – 13

Ace - 1

Please note here, though Ace has a numerical equivalent value of 1, it is always considered as the top-rated card. So it is also included in the list of high cards.

The game organizer selects N cards and places it in the deck face-down on the table. Player A turns over the top card and places it on a pile; then player B turns over the top card and places it on the same pile. A and B alternate turns until the N cards are exhausted. The game is scored as follows:

if a player turns over an ace that is 1, with at least 4 cards remain to be turned over, and none of the next 4 cards is a high card, that player scores 4 points

if a player turns over a king that is 13, with at least 3 cards remain to be turned over, and none of the next 3 cards is a high card, that player scores 3 points

if a player turns over a queen that is 12, with at least 2 cards remain to be turned over, and none of the next 2 cards is a high card, that player scores 2 points

if a player turns over a jack that is 11, with at least 1 card remains to be turned over, and the next card is not a high card, that player scores 1 point

Write a program to calculate the scores of the two players.
"""


n = int(input())
arr = []
for i in range(0,n):
    x = int(input())
    if x==1:
        x=14
    arr.append(x)
st=0
a=0
b=0
for i in range(0,n):
    if arr[i]>10:
        for j in range(1,arr[i]%10+1):
            if i+j<n:
                if (arr[j+i]>10):
                    st=1
                    break
            else:
                st=1
                break
        if(st==0):
            if(i%2==0):
                a=a+arr[i]%10
                print("Player A scores "+str(arr[i]%10)+" point(s)")
            else:
                b=b+arr[i]%10
                print("Player B scores "+str(arr[i]%10)+" point(s)")
        st=0
print("Player A: "+str(a)+" point(s)")
print("Player B: "+str(b)+" point(s)")