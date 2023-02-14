'''
Instance and class variables
'''

class Employee:
    no_of_leaves = 8 # these are the class variables. A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.
    pass


harry = Employee()
rohan = Employee()



harry.name = 'Harry' # these are all the instance variables. If the value of a variable varies from object to object, then such variables are called instance variables.
harry.salary = 45500
harry.role = 'Instructor'


rohan.name = 'Rohan'
rohan.salary = 4500
rohan.role = 'Student'

# to change the class variables we can change like as follow
print(Employee.no_of_leaves)
Employee.no_of_leaves = 9
print(Employee.no_of_leaves)

# to change the instance variable while not changing the class variable we can follow this
print(rohan.no_of_leaves)
rohan.no_of_leaves = 12
print(rohan.no_of_leaves)
print(Employee.no_of_leaves) #this only changes no_of_leaves for rohan and not for the whole employee instance


# __dict__ attribute : All objects in Python have an attribute __dict__, which is a dictionary object containing all attributes defined for that object itself. The mapping of attributes with its values is done to generate a dictionary.

print(rohan.__dict__)
print(harry.__dict__)
print(Employee.__dict__)
# Note: In case of harry we wont wint no_of_salary key in the dictionary. Since we have only created that instance variable for rohan only.
# by changing the instance variable no effect is seen on the class variable. But by changing the class variable, all the instance variables are changed.
# Class variables are shared across all instances. but instance variable is personal for each instance.