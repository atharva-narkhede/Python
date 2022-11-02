#Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which wins. If it's a drawing print D. Use Dictionary concept to get the result.





# You are using Python
beats = {'P': 'S',
         'R': 'P',
         'S': 'R'}

p = input()
p_lst = p.split()


if p_lst[0] == beats[p_lst[1]]:
    print(p_lst[0])
elif p_lst[1] == beats[p_lst[0]]:
    print(p_lst[1])
elif p_lst[0] ==  p_lst[1]:
	print('D')