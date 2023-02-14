'''
Polymorphism: Polymorphism is a fundamental concept in object-oriented programming that allows objects of different types to be treated as if they are of the same type. 
In Python, polymorphism is achieved through the use of methods that have the same name but are defined in different classes.

There are two main types of polymorphism in Python:

Method overloading: Method overloading allows a class to have multiple methods with the same name but different parameters. 
When a method is called, Python determines which version of the method to call based on the arguments passed to it.

Method overriding: Method overriding allows a subclass to provide a different implementation of a method that is already defined in its parent class. 
When a method is called on an object of the subclass, the overridden version of the method is called instead of the one in the parent class.

Polymorphism is a powerful tool that allows for code reusability, flexibility, and extensibility. 
By treating different objects as if they are of the same type, it becomes easier to write generic code that can work with a variety of different objects.
'''

# this can be an example of polymorphism
print(5+6)
print("5"+"6")