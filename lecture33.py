'''
Scope, Global Variables, Global Keywords
'''

# Global Variables: Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# Scope: In programming, the scope of a name defines the area of a program in which you can unambiguously access that name, such as variables, functions, objects, and so on.
# he Python scope concept is generally presented using a rule known as the LEGB rule. The letters in the acronym LEGB stand for Local, Enclosing, Global, and Built-in scopes.

# Global scope: The names that you define in this scope are available to all your code.

# Local scope: The names that you define in this scope are only available or visible to the code within the scope.

# Global variable cannot be changed in the local scope as:

from ast import Global


l = 4


def my_function_1(k):
    print(l)
    # l = l+45  # this will throw error as you cannot change the global variable in locally


my_function_1("hello")

# Global Keyword: To attain the permission to use the change global keyword locally, we use global keyword. To use global keyword we use global variable_name as

l = 4


def my_function_2(k):
    global l
    l = l+45
    print(l)


my_function_2("hello")
print(l)

# Note: After changing the global variable in the local scope using global keyword, the value of the global variable is changed for all the program and not just for the local scope.


# Nested Functions: Function inside a function is called a nested function

def harry():
    x = 20  # defining the local variable

    def rohan():
        # changing the global variable x. If this is not present in global scope it will create it. Note that this will change the value of variable present in global scope and not in local scope (harry).
        global x
        x = 88  # changing the value of x for global scope

    print('before calling rohan x=', x)  # x = 20
    rohan()  # calling the nested function rohan()
    # x = 20, Since value is changed for global scope and not for the local scope harry.
    print('after calling rohan x=', x)


harry()
print(x)  # x = 88, Since we have created a global variable in the nested function rohan()
