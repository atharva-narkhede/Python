#The Encryption Algorithm: Encrypt the given input with these steps.
#Eg: apple
#Step 1:
#Reverse the input (elppa)
#Step 2:
#Replace the below letters using the given values (1lpp0)
#Step3:
#Add 'aca' to the end of the word. (1lpp0aca)



def encrypt(word):
    v= {'a':'0','e':'1','o':'2','u':'3'}
    return ''.join(v[i] if i in v else i for i in word[::-1]) +'aca'
    
    
word = input()
print(encrypt(word))
