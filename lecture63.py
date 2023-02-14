'''
Specifiers: In Python, specifiers (also known as access modifiers or visibility modifiers) are keywords that are used to control the visibility and accessibility of attributes and methods in a class. 
Specifiers help to enforce encapsulation and make the class more secure and robust.
There are three types of specifiers in Python:

Public: The public specifier is the default specifier in Python. 
It indicates that an attribute or method is accessible from anywhere in the program. 
In Python, all attributes and methods that do not start with an underscore are considered public.

Protected: The protected specifier is indicated by a single leading underscore before the name of an attribute or method. 
It indicates that an attribute or method is accessible within the class and its subclasses, but not from outside the class.

Private: The private specifier is indicated by a double leading underscore before the name of an attribute or method. 
It indicates that an attribute or method is accessible only within the class itself, and not from outside the class or its subclasses.

It's worth noting that while Python has these specifiers, they are not strictly enforced by the language itself. 
Instead, it is up to the programmer to follow these conventions and respect the visibility and accessibility of the attributes and methods in a class.
'''

class Employee:
    no_of_leaves = 8 
    _protected_variable = 9 # to create a protected variable just use _ before variabele name
    __private_variable = 10 # to create a private variable just use __ before variabele name


    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def __init__(self, name_argument, salary_argument, role_argument): # this is how we create a constructor
        self.name = name_argument
        self.salary = salary_argument
        self.role = role_argument

    @classmethod
    def change_no_of_leaves(cls, new_no_of_leaves):
        cls.no_of_leaves = new_no_of_leaves

# below class method takes a string and return an instance in class Employee, such that it splits the string and creates value of different instance variable
    @classmethod
    def from_str_to_class(cls, str_to_class):
        return cls(*str_to_class.split('-'))

# below method is used to create a static method. The reason we defined it in class and not outside class is because sometimes we need some methods to be executed only for the objects and not for any other variable.
    @staticmethod
    def printgood_method(string_as_input):
        print("This is good "+ string_as_input)

# to inherit from class Employee into Programmer class
class Programmer(Employee):
    # we can also add new class variables as
    no_of_holidays = 12
    def printprog(self): # to create something in Programmer class that is not already present in Employee class
        return f"The Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role}. The language used in {self.language}"

    # we can also create a new constructor for the Programmer class which will be little differnt from Employee class
    def __init__(self, name_argument, salary_argument, role_argument, language_argument): # Note we can use super to copy all the arguments of the constructor that are common between both Empoloyee class and Programmer class This is not the right way.
        self.name = name_argument
        self.salary = salary_argument
        self.role = role_argument
        self.language = language_argument

harry = Employee('Harry', 45500,'Instructor')
# to access the protected variable you can directly use this
print(harry._protected_variable)

#but to access the private variable you cant actually us print(harry.__private_variable), but you have to use the name mangling which is done as
print(harry._Employee.__private_variable) # i.e., instanceName._ClassName__privateVariableName

# The purpose of name mangling is to avoid naming conflicts between attributes and methods in different classes, and to provide a way for classes to define "private" attributes and methods that are not accessible from outside the class. 
# By making the name of an attribute or method more unique, it becomes less likely to be accidentally overwritten or accessed from outside the class.
# Name mangling is a technique used in Python to make a class attribute or method name more unique by adding a double underscore prefix to its name.
# When a name is "mangled" in this way, its actual name in the class becomes _classname__name, where classname is the name of the class that owns the attribute or method, and name is the original name of the attribute or method.
