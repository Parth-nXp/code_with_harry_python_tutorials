'''
Claass Method: a class method is a method that is bound to the class and not the instance of the class. 
It can be called on the class itself and does not depend on the state of any particular instance.

A class method is defined using the @classmethod decorator and takes the class as its first argument, conventionally named cls. 
Class methods are commonly used for methods that need to access or modify class-level variables, perform some setup or initialization tasks for the class, or to create new instances of the class.
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
    def change_no_of_leaves(cls, new_no_of_leaves):   # here cls is present instead of self because we dont want to change the no_of_leaves for any instance but we want to change it for whole class.
        cls.no_of_leaves = new_no_of_leaves

harry = Employee('Harry', 45500,'Instructor')
rohan = Employee('Rohan', 4500, 'Student')


harry.change_no_of_leaves(10) # using classmethod we can change the class varviable with the use of instance variable.

print(harry.no_of_leaves)