'''
Inheritance: Inheritance is a powerful object-oriented programming concept in Python (and many other programming languages) that allows a new class to be based on an existing class. 
Inheritance is a way to create a new class that is a modified or specialized version of an existing class, with some or all of the same attributes and behaviors. 
The existing class is called the base class or parent class, and the new class is called the derived class or child class.

In Python, inheritance is achieved by using the keyword class and a set of parentheses in the definition of a derived class, followed by the name of the base class. 
The derived class inherits all of the attributes and methods of the base class, and can add its own attributes and methods or modify the behavior of the base class.

With inheritance, we can create complex class hierarchies that reflect the relationships between different types of objects, and reuse code from existing classes, making our programs more efficient and easier to maintain.
'''
# Single Inheritance: Single inheritance is a type of inheritance in object-oriented programming where a derived class inherits the attributes and methods of a single base class. 
# In other words, a derived class can have only one parent or base class. 
# Single inheritance is a useful and straightforward way to reuse code and create a hierarchy of classes that reflect the relationships between different types of objects. 
# However, it can be limiting in some cases, especially when dealing with complex class relationships that require multiple inheritance or other advanced features.

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
rohan = Employee('Rohan', 4500, 'Student')

# below will create instance of Programmer class using the inherited instance
shubham = Programmer('Shubham', 100000, 'Programmer', 'Python')
karan =Programmer.from_str_to_class('Karan-150000-Programmer-Python')

print(karan.printprog()) # Method from Programmer class
print(karan.printdetails()) # Method from Employee class
print(karan.no_of_holidays)