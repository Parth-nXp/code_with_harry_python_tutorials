'''
Functions : If you want to exeecute a part of code again and again you use function. This saves you from writing that part of code again and again
'''
# Bulit in functions
a = 9
b = 7
# sum is a built in function. You can open the built in function by pressing ctrl and left mouse button
c = sum((a, b))
print(c)

# User defined functions


def function1():  # defining the function name
    # action which the function will perform
    print("Hello you are in function 1")


function1()  # calling the function

# function that can input the values too


def function2(a, b):
    print("Sum of the numbers you have input is ", a + b)


function2(1, 3)


# if you want to save the value of the function in any variable

def function3(a, b):
    average = (a+b)/2
    return average  # if this return is not used than you will get none as output when you will print the value v in main code


v = function3(6, 8)
print(v)
# Docstring


def average_of_number(a, b):
    """This functions finds the average of the two numbers. This function only works for two numbers.

    Args:
        a (int, float): This is the first number
        b (int, float): This is the second number
    """
    average = (a+b)/2
    return average


print(average_of_number.__doc__)
