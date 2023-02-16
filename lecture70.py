'''
Object Introspection: Object introspection is the ability of a program to examine the properties and methods of an object at runtime. 
In Python, you can use the built-in functions dir() and type() to perform object introspection.

In addition to these built-in functions, Python provides several other tools for performing object introspection, including the inspect module and the __dict__ attribute. 
With these tools, you can examine the properties and methods of objects in more detail, and even modify them at runtime.

Object introspection is a powerful tool for debugging and dynamic programming in Python, allowing you to inspect and modify objects at runtime, and to build more flexible and adaptable programs.
'''

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email =  f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property # using this property decorator we dont need to call self.email() method instead we can call it directly as a property self.email
    def email(self):
        if self.fname == 'None' and self.lname == 'None':
            return "Email is not set. Please set it using setter."
        return f"{self.fname}.{self.lname}@codewithharry.com"
    
    # now suppose we wan to change the first name and the last name after changing the email. we can use the setter as
    @email.setter
    def email(self,string):
        print('Setting now...')
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    # to delete any attribute we generally use the del attribute. Suppose we want ot deleter the email attibute, we generally dont delter the attribute else we just set it to none as
    @email.deleter
    def email(self):
        self.fname = 'None'
        self.lname = 'None'
        #after this we will create if condition in the email function


skillf = Employee("Skill", "F")
print(skillf.email)


# id(): In Python, the id() function returns a unique identifier (an integer) for an object. 
# The identifier is guaranteed to be unique and constant for the lifetime of the object.
# The id() function is useful for low-level memory management and debugging, but it is generally not needed for normal Python programming. 
# Most Python programs can be written without ever using the id() function.
# all objects have there unique id. no two objects can have same id

print(id("this is a string"))


# dir(): In Python, the dir() function returns a list of all the valid attributes and methods of an object. 
# You can call dir() on any object to see what attributes and methods are available.
# The output of the dir() function includes all the built-in attributes and methods of the object, as well as any user-defined attributes and methods. 
# The output is sorted alphabetically, and may include some attributes and methods that are not meant to be used directly.
# The dir() function is commonly used for exploring and debugging Python code. 
# You can use it to see what methods and attributes are available for a given object, and to explore the internal workings of Python modules and packages. 
# It is especially useful for working with complex objects and libraries, where the available methods and attributes may not be immediately obvious.

print(dir("this is a string"))
print(dir(skillf))


# inspect.getmembers(): inspect.getmembers() is a built-in Python function that returns a list of all the attributes and methods of an object. 
# It is similar to the dir() function, but provides more information about each attribute and method.
# The getmembers() function takes two arguments: an object, and an optional predicate function. 
# If a predicate function is provided, it is used to filter the list of attributes and methods. 
# The output of getmembers() is a list of 2-tuples, where each tuple contains the name of the attribute or method, and its value.
# The getmembers() function is commonly used for inspecting and debugging Python code. 
# It provides more information than the dir() function, and can be used to explore the internal workings of complex objects and libraries.

import inspect
print(inspect.getmembers(skillf))