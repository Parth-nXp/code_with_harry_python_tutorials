'''
self & __init__() (Constructors)
'''


# Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.
class Employee:
    no_of_leaves = 8 

# method: In Python, a method is a function that is associated with an object, and can be called on that object using dot notation.
# It typically performs some operation on the object, and may or may not take additional arguments.
# Methods are defined within a class, and are used to provide functionality specific to that class.
# Some examples of built-in methods in Python include sort() for lists, append() for lists and dictionaries, and upper() for strings.
# Users can also define their own methods within their own classes.
    def printdetails(self): # this generates a method. here self means an object. Suppose if we want to run printdetails on the object rohan then self will be replaced by rohan.
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


# Constructor: In Python, a constructor is a special method that is called when an object is created from a class.
# The constructor method is typically used to initialize the instance variables of the object, and can take one or more parameters.
# The constructor method in Python is always named __init__() and is defined within the class.
# When an object is created, Python automatically calls this method to initialize the object's attributes.
    def __init__(self, name_argument, salary_argument, role_argument): # this is how we create a constructor
        self.name = name_argument
        self.salary = salary_argument
        self.role = role_argument
        

harry = Employee('Harry', 45500,'Instructor') # this is how we create an object from the constructor
rohan = Employee('Rohan', 4500, 'Student')




print(rohan.printdetails()) # this is how we print details on the object rohan then self will be replaced by rohan. This calls method printdetails from class Employee