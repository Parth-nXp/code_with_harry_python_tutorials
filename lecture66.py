'''
Diamond Shaped problem: The diamond-shaped problem is a common issue that arises in multiple inheritance when a subclass inherits from two or more classes that have a common ancestor. 
The problem gets its name from the diamond shape that is formed when the class hierarchy is represented graphically.
'''

class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(C,B): #will print This is a method from class C
#class D(B,C): #will print This is a method from class B
    pass


a = A()
b = B()
c = C()
d = D()

d.met()