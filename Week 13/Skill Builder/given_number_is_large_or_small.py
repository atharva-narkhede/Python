#Write a program to assume an integer and find whether the given number is large or small than the given input. 
#If the number is above or below the user input throw the user-defined exception as “Value is Small” or “Value is large”. 
#If it matches with the user assumption display the message as “Well Done”. 
#This process should be continued till the user prompts the symbol $. 



x = int(input())
ch = 'y'

while (ch != '$'):
    try :
        n = int(input())
        if n<x :
            raise Exception('Value is small')
        elif n>x :
            raise Exception('Value is large')
        else :
            print("Well Done")

    except Exception as e:
        print(e)
    
    ch = input()[0]
