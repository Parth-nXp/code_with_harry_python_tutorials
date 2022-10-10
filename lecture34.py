'''
Recursions: Recursive Vs Iterative Approach
'''

# Iteration: Iteration is repeated execution of a set of statements .
# Recursion: Recursion is a way of programming in which function call itself until it reaches some satisfactory condition.


def print2(str_1):
    # print2(str_1) # calling a function inside a same function will cause an error. Since we have called a function but havent told program when to stop calling the function, so it will keep on repeating the function until the program throws the error.
    # Note: Function is called 996 times maximum
    print('This is ' + str_1)


print2('Harry')


# Factorial function using the iterative approach.

def factoraial_iterative(n):
    """This function gives the factorial of the number

    Args:
        n (int): any number whose factorial you want to find
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return(fac)


number = int(input("Enter a number whose factorial you want to calculate"))
print(factoraial_iterative(number))


# Factorial function using the recurssive approach
def factorial_recurssive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recurssive(n-1)


'''
5* factorial_recurssive(4)
5 * 4 * factorial_recurssive(3)
5 * 4 * 3 * factoarial_recurssive(2)
5 * 4 * 3 * 2 * factorial_recurssive(1)
now factorial_recurssive(1) == 1
So return now will be 5 * 4 * 3 * 2 * 1 = 120
'''


print(factorial_recurssive(number))


# Quiz: Fibonnaci using recurssion


def fibonnaci(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonnaci(number-1) + fibonnaci(number-2)


print(fibonnaci(100))


# Recursion is used when we have got simple program as it makes things simpler, less code to write, but is difficult to dubug as it is really tricky to back track.
# Iteration is used when we have got a big and complex code as it is really simpler to debug the code.
