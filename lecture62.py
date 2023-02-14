'''
Multilevel Inheritance: Multilevel inheritance is a type of inheritance in object-oriented programming in which a derived class is created by inheriting from a base class, and that derived class is then used as the base class for another derived class. 
In other words, a derived class is used as a base class for another derived class, creating a hierarchy of inheritance.
In Python, multilevel inheritance is achieved by defining a base class, a derived class that inherits from the base class, and another derived class that inherits from the first derived class.
Multilevel inheritance can be a useful way to create complex class hierarchies that reflect the relationships between different types of objects. 
However, it can also lead to code that is hard to read and understand, and can introduce dependencies and potential conflicts between the different classes. 
Therefore, it should be used judiciously and with a clear understanding of its potential advantages and drawbacks.
'''

# When a variable is accessed in a derived class, Python first looks for that variable in the derived class itself. 
# If the variable is not found there, Python then searches for the variable in the immediate parent class of the derived class, and then in the parent class of that parent class, and so on, until it reaches the top of the inheritance hierarchy.
class Dad:
    basketball =1

class Son(Dad):
    Dance = 1
    def isdance(self):
        return f"Yes I dance {self.Dance} number of times"

class Grandson(Son):
    Dance = 6
    def isdance(self):
        return f"Yes I dance awesomly {self.Dance} number of times"


darry = Dad()
larry = Son()
harry = Grandson()

print(harry.basketball)