'''
Abstract base class: An Abstract Base Class (ABC) is a special type of class in Python that cannot be instantiated on its own, but is instead intended to serve as a base class for other classes. 
It provides a way to define a common interface that derived classes must implement, but allows for variations in implementation. 
In essence, an ABC defines a set of methods that must be implemented by any concrete class that inherits from it.
ABCs provide a way to define a common interface for a set of related classes, while still allowing for variation in implementation. 
They can be used to ensure that derived classes conform to a specific API, and can help to make code more modular, extensible, and maintainable.

Abstact Method: In Python, an abstract method is a method that is declared in an abstract class but does not have an implementation. 
An abstract method serves as a placeholder that must be implemented by any concrete subclass that inherits from the abstract class.
Attempting to instantiate an object of an abstract class, or a subclass that doesn't implement all the abstract methods of its abstract parent class, will result in a TypeError. 
This is because abstract classes are not intended to be instantiated on their own, but rather provide a common interface and shared behavior that concrete subclasses can inherit and implement.
Abstract methods and classes are commonly used in Python for creating frameworks and APIs that enforce a common structure and behavior across a set of related classes, while still allowing for variation and customization in implementation.

'''

from abc import ABC, abstractmethod

class Shape(ABC): # using this we can force the printarea method to all the objects. If we wont define the printarea method it will throw an error.
    @abstractmethod
    def printarea(self): 
        return 0 


class Rectangle:
    type ="Rectangele"
    sides = 4
    def __init__(self):
        self.length = 6
        self.width = 7


    def printarea(self): # this method is compalsury to be defined or else you will get an error
        return self.length * self.width


rect1 = Rectangle()
print(rect1.printarea())

# note: you cannot make the object directly using the abstract base class like this:
# tryobj = Shape()
