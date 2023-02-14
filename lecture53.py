'''
Creating the first class in the OOPS program. 
'''

class student: # create a class called student
    pass # if you want python program to perform nothing, you use the pass method

harry = student() # this creates an object harry from the class student
larry = student()

print(harry, larry) # it will print two different memory locations proving that these two are two different objects

# we can actually add content to these objects as follows

harry.name = "Harry"
harry.std = 12
harry.section = 'A'

print(harry.section)