'''
OS module
'''

import os # built-in module, stands for operating system

#print(dir(os)) # object introspection, all the things we can do with the os module

# to check our current working directory
print(os.getcwd()) # get current working directory


# to chnage current working directory
#os.chdir("D:/")
#print(os.getcwd())


# to get all the files name in the current working directory
print(os.listdir()) # list directory

# to check files in any specific directory simply pass that directory path as the argumeent as
print(os.listdir("D:/")) # this returns as a list datatype

# to creake a folder
# os.mkdir("This")

# to make folder inside a folder, that is making directories
#os.makedirs("This\that")

# to change name of any file in the current working directory
# os.rename("harry.txt","codewithharry.txt") 

# to get the environment variable
print(os.environ.get("PATH"))

# To join two paths to make one 
print(os.path.join("D:/","/python tutorials"))

# To check if any path exists or not
print(os.path.exists("D:/")) # if true it exists, if false it does not exist

# to check if any path is file or directory
print(os.path.isfile("D:/")) # to check if file or not
print(os.path.isdir("D:/")) # to check if directory or not