'''
seek(), tell() and more python functions for file
'''

# tell(): Gives the pointer position in the file

file_1 = open("harry.txt")

# Tell the position of the pointer which is at 0 at this point
print(file_1.tell())
print(file_1.readline())  # Read the first line and update the pointer
print(file_1.tell())  # Tells the updated pointer position
print(file_1.readline())  # Reads the second line and update the pointer
print(file_1.tell())  # tells the updated pointer position
file_1.close()


# seek(): update the pointer position with the arguments given in the function

file_2 = open("harry.txt")

print(file_2.readline())  # read the first line and update the pointer
file_2.seek(0)  # set the new pointer position to 0
print(file_2.readline())  # read the line from the updated pointer position
