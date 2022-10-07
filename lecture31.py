'''
Using With block to open the python file
'''

# reads the file using the with block. Works same as file_1 = open("harry.txt"). Using with block to open file, you dont need no close the file. With block will automatically close the file.
with open("harry.txt") as file_1:
    char = file_1.readlines()
    print(char)


# Question of the day: If the file is again opened outside the with block(), will it be able to open the file and read it?

file_1 = open('harry.txt', 'rt')
print(file_1.readlines())
