#Peter and Casino 

#Hotel Royal Gardenia has arranged for an elite business party for the lead industrialists and celebrities of the City. Followed by a dinner buffet, the Event coordinators planned for some casino game events for the high-toned crowd. Peter was a visitor at the party and he takes some number of rubles to the casino with the intention of becoming rich. He plays three machines in turn. Unknown to him, the machines are entirely predictable. Each play costs one ruble. The first machine pays 20 rubles every 25th time it is played; the second machine pays 80 rubles every 120th time it is played; the third pays 8 rubles every 12th time it is played.

#Given the number of rubles with Peter initially (there will be at least one and fewer than 1000), and the number of times each machine has been played since it last paid, write a program that calculates the number of times Peter plays until he goes broke.


n = int(input())
m1=int(input())
m2=int(input())
m3=int(input())
p=0
if m1>=25:
        n=n+20*(m1//25)
        m1=m1%25
if m2>=120:
        n=n+80*(m2//120)
        m2=m2%120
if m3>=12:
        n=n+8*(m3//12)
        m3=m3%12
while(n>0):
    m1+=1
    n-=1
    p+=1
    if m1>=25:
        n=n+20*(m1//25)
        m1=m1%25
    if n>0:
        m2+=1
        n-=1
        p+=1
    else:
        break
    if m2>=120:
        n=n+80*(m2//120)
        m2=m2%120
    if n>0:
        m3+=1
        n-=1
        p+=1
    else:
        break
    if m3>=12:
        n=n+8*(m3//12)
        m3=m3%12
print(""+str(p)+" times")