'''
Args and Kwargs
'''

# *args- *args in function definiton in python is used to pass avariab;e number of arguments to a function.
# It is used to pass a non0key worded, variable length argument list

from keyword import kwlist


def funcargs(*args): # defining the fucntion with use of args.  Always look for * sign before passing it as arg in the function
    print(type(args)) # printing the type of args which is always by convention tuple, even if you pass the args as list it will change it to tuple
    print(args[0]) # printing the first element of the arg
    for item in args: #for loop to print all the elements of the args tuple
        print(item)


name_list = ["Harry", "Rohan", "Hammad", "Skillf", "Shivam"] # a list which is passed as args in the function

funcargs(*name_list) # calling a function with args, always check for the * sign before list name while passing it as a arg.


# you can also pass the normal arguments in the function, but always notice to add normal arguments before the *args or it will show an error.

def funcargs2(norm, *args):
    print(norm)
    for item in args:
        print(item)

normal = "I am normal argument and these names below are args:"
funcargs2(normal, *name_list)

#using below will throw an error

'''
def funcargs2(*args, norm)


funcargs(*name_list, normal)
'''


# **kwargs- **kwargs is a function definitions in python is used to pass a keyworded, variable-lenth argument list.
# convention while passing the arguments are 1) normal argyuments 2) *args arguments 3) **kwargs arguments
def funcargs2(norm, *args, **kwargs):
    print(norm)
    for item in args:
        print(item)

    print('\n')
    print('These are some of our heroes')

    for key, value in kwargs.items():
        print(f'{key} is our {value}')

kw_list = {"Harry": "Monitor", "Rohan": "Fitness Instructor", "Hammad": "Cook"}
funcargs2(normal, *name_list, **kw_list)



# we can write *args and **kwargs with any name but it is convention to use these naming only.