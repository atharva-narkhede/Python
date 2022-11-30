#Function Overloading
#Create a function 'add'. The function add should perform the following operation.
#The first argument should be the data type of the remaining arguments (str or int) (inp_type)
#It should be able to get any number of arguments (inp1, inp2, inp3,....)
#if the data type is 'str', it should perform string concatenation
#if the data type is 'int', it should perform addition


def add(datatype, *args):
    
    if datatype == 'int':
        answer = 0
        for x in args:
            answer = answer + int(x)
            print(answer)
        
    if datatype == 'str':
        answer = ''
        for x in args:
            answer = answer + x
            print(answer)
    
inp_type = input()
inp1 = input()
inp2 = input()
inp3 = input()
add(inp_type,inp1,inp2,inp3)