#Write a program to sort a tuple of tuples by 2nd item

def Sort_Tuple(tup):
	
	
	lst = len(tup)
	for i in range(0, lst):
		
		for j in range(0, lst-i-1):
			if (tup[j][1] > tup[j + 1][1]):
				temp = tup[j]
				tup[j]= tup[j + 1]
				tup[j + 1]= temp
	return tup


tup =[('for', 24), ('is', 10), ('Coimbatore', 28),('Collections', 5), ('Towncity', 20), ('a', 15)]
		
print(Sort_Tuple(tup))