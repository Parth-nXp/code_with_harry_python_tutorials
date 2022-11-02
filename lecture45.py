'''
Import statement
'''

import sys #The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. 
# It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.

print(sys.path) # It contains a list of directories that the interpreter will search in for the required module. 



# importing variables from one another file with name file_2

import file_2 # first we will import all the contents of the file_2
print(file_2.a) # this will print the value of the variable a in the file_2

# you can also directly access the value of a without writing file_2.a but you can directly write a as

from file_2 import a # this will import a from file_2 so that we can directly use this variable as a
print(a) # this will print the value of the variable a in the file_2
# Note that this method is not suggested so always use file_2.a instead


# to chnage the value of the variable a in the file__2
file_2.a = 'hello' # this will write the value of a in the file_2
print(file_2.a) # this will print the value of the variable a in the file_2


# to access any function from the file_2

file_2.printjoke("This is me")
