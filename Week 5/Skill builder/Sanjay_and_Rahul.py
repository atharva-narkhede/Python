#Sanjay and Rahul have a set of color crayons. Sanjay has a set of colors whereas Rahul has a set of colors. Write a program to find the colors they have in common. Print the colors that Rahul has but not Sanjay. Sanjay lost his Green color. Update this information. 
#Note: Sort the sets before printing


# You are using Python
list1 = input().split()
list2 = input().split()
set1 = set(list1)
set2 = set(list2)
print(sorted(set1 & set2))
print(sorted(set2.difference(set1)))
set1.remove('green')
print(sorted(set1))