#Bowman planned a vacation to Alphabet Land.
n = int(input())
recipies_list = []
for i in range(n):
    recipies_list.append(input())
bags = len(set(recipies_list))
sorted_recipies = sorted(set(recipies_list))
print(bags)
for recipie in sorted_recipies:
    for i in range(n):
        if recipie == recipies_list[i]:
            print(i+1,end = " ")
    print()
