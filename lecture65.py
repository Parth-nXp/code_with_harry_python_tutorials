'''
Overriding: Overriding is a fundamental concept in object-oriented programming that allows a subclass to provide a different implementation of a method that is already defined in its parent class. 
In Python, method overriding is achieved by redefining a method in the subclass with the same name as the method in the parent class.

When a method is called on an object of the subclass, Python first looks for the method in the subclass. 
If the method is found, the overridden version of the method is called instead of the one in the parent class.
'''

class A:
    classvar1 = 'I am a class variable in class A'

    def __init__(self):
        self.var1 = 'I am a class variable in class A\'s constructor'
        self.classvar1 = 'Instance var in class A'
        self.special = 'Special'

class B(A):
    classvar2 = 'I am a class variable in class B'

    def __init__(self): # This is how we have override a constructor
        super().__init__() # in case if we have override a constructor but still we need some variable from the parent constructor (say special) then we have to type this to avoid any error
        self.var1 = 'I am a class variable in class B\'s constructor'
        self.classvar1 = 'Instance var in class B'
        #super().__init__() # note: if this is written below and now we call any instance variable lets say var1, it will print var1  of class A. since at last it has called the constructor of its parent.
        print(super().var1) # this prints the class variable of the parent class

a = A()
b = B()

print(b.special)