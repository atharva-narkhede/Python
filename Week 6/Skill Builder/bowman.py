#Bowman planned a vacation to Alphabet Land. He had to solve a problem to enter Alphabet Land. 
#He was given N recipes made up of lower case English alphabets. The recipes were indexed from 1 to N. R[1], R[2], ….., R[N]. 
#He had to group identical recipes and put them into bags. Help Bowman print the indices of the recipes in each bag.


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
