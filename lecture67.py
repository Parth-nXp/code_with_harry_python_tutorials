'''
Dunder method: Dunder (double underscore) methods, also known as magic methods or special methods, are a set of predefined methods in Python that begin and end with two underscores (e.g., __init__, __str__, __add__). 
These methods provide a way to define custom behavior for built-in Python operators and functions, such as +, -, *, /, ==, [], and many more.
Dunder methods are a powerful feature of Python and are used extensively in many standard libraries and frameworks.
They allow for a more intuitive and expressive syntax, and can make code easier to read and maintain.'


Operator overloading: Operator overloading is the process of defining custom behavior for built-in operators and functions in a class. 
In Python, operator overloading is implemented using dunder (double underscore) methods, also known as magic methods or special methods.
Operator overloading is a powerful feature in Python and is used extensively in many standard libraries and frameworks. 
It allows for a more intuitive and expressive syntax, and can make code easier to read and maintain. 
However, it should be used with caution, as it can make code less predictable and harder to understand if overused or used inappropriately.

To overwite any overloading operator, simply search Mapping operators to functions
'''

class Employee:
    no_of_leaves = 8 

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def __init__(self, name_argument, salary_argument, role_argument): # this is how we create a constructor
        self.name = name_argument
        self.salary = salary_argument
        self.role = role_argument

    @classmethod
    def change_no_of_leaves(cls, new_no_of_leaves):
        cls.no_of_leaves = new_no_of_leaves
    
    def __add__(self, other): # Dunder method helping in operator overloading
        return self.salary + other.salary
    
    def __repr__(self): # Dunder method not helping for opertaor overlaoading
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    def __str__(self): # Dunder method not  helping for opertaor overlaoading
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 = Employee('Harry', 345, 'Programmer')
emp2 = Employee('Rohan', 85, 'Cleaner')

print(emp1 + emp2) # this function doesnt know what to add with this. So will thorugh error. To avoid any error, we actually need to define the function of what to add. that function is called Dunder method or special functiopn

print(emp1) # this generally returns the memory location of the emp1 object. But we can actually do what to do with this using the __repr__ method