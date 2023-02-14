'''
Decorators: They modify the functionality of the function. This is used if we need to do many things with the same function we can actually define that function as a decorator. 
'''

def function1(): # create a function with the name 'function1'
    print("Subscribe now")  # this function prints the name 'subscribe now'

function2 = function1 # create a function with the name 'function2' and it is a copy of the function1

del function1 # delete the function

function2() # this will print the name 'function 2' as already a copy is created.


# creating a function inside a function


def funcret(num):
    if num == 0:
        return print # it is a built-in function print
    elif num == 1:
        return sum # it is a built-in function sum

a = funcret(0)
print(a)

# we can also return a function from a function

def executer(func):
    func("Hello, world!")


executer(print) # this executes the executer function with argument as a function which is print.


# Using a decorator function

def dec1(func1): # creating a decorator with the name 'dec1'
    def nowexec(): # creating a function in the decorator with name 'nowexec' which will be called everytime decorator is called
        print("Now executing")
        func1() # func1() function will be called everytime in between the commands above and below it
        print("Executed")
    return nowexec # nowexec function is called. or calling a function inside a function

@dec1 # defining that who_is_harry function will always be executed using the decorator dec1
def who_is_harry():
    print("Harry is a good boy")


who_is_harry() # calling the function who_is_harry with the decorator 