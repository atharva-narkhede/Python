#Write a program that accepts n numbers from the user, stores them in a tuple and sorts the tuple, and checks whether an element occurs in the tuple or not.

# You are using Python
n =int(input())

num_list = []

for i in range(n):
    num_list.append(int(input()))
search_element = int(input()) 
num_tuple= tuple(num_list) 
for num in num_list:
    if num== search_element: 
        print("The element is present in the list")
        break
else:
    print("The element is not present in the list") # 
print("The elements in the tuple are:", num_tuple)
num_list=sorted(num_tuple)
print("The sorted elements of the tuple are:", num_list)