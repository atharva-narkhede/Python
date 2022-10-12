#Given a number N followed by 2 lists A and B of N integers each. Form a 3rd list C of size N where each element of list C is the sum of the respective elements in lists A and B.

#Note: Use zip() and sum() function

N = int(input())
list1 = input().split()
list2 = input().split()


for i in range(0,len(list1)):
    list1[i] = int(list1[i])
    list2[i] = int(list2[i])
    
# using zip() + sum() to add two list  
res_list = [sum(i) for i in zip(list1, list2)] 
  
# printing resultant list  
print (*res_list) 
