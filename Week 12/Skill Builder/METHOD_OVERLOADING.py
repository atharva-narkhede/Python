#METHOD OVERLOADING
#Create a class named 'Hello'. Define a method 'sayHello'
#Create an object obj.
#Call method 'sayHello' without argument, Output should display 'Hello'.
#Call method 'sayHello' with one argument, Output should display 'Hello 'argument value'' (Ex: If the argument passed is 'John' Output should display 'Hello John'


class Hello:
    
    def sayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello')
            
inp = input()
obj = Hello()
obj.sayHello()
obj.sayHello(inp)