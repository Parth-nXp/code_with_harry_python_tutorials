'''
Static Methods: In Python, a static method is a method that belongs to a class, but does not have access to the class or instance. 
It is defined using the @staticmethod decorator and does not take any special first argument like self or cls. 
It is a regular method that operates on data that is passed to it as arguments, and does not modify any class or instance state.

Static methods are used when a method does not depend on the state of a specific instance or the class, but is related to the class in some way. 
Static methods are often used for utility functions that perform a specific operation that is related to the class, but does not require any instance data.
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

# below class method takes a string and return an instance in class Employee, such that it splits the string and creates value of different instance variable
    @classmethod
    def from_str_to_class(cls, str_to_class):
        return cls(*str_to_class.split('-'))

# below method is used to create a static method. The reason we defined it in class and not outside class is because sometimes we need some methods to be executed only for the objects and not for any other variable.
    @staticmethod
    def printgood_method(string_as_input):
        print("This is good "+ string_as_input)

harry = Employee('Harry', 45500,'Instructor')
rohan = Employee('Rohan', 4500, 'Student')
karan = Employee.from_str_to_class('Karan-12000-Student')


karan.printgood_method('Harry')
Employee.printgood_method('Rohan')
