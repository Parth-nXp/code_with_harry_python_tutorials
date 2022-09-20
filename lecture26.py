'''
File Writing
'''
file_1 = open("harry.txt")  # this returns a file pointer
content_1 = file_1.read()  # exploiting the pointer with read method
print(content_1)  # printing all the information that is saved in the variable content

# closing the file after performing all the necessary operations on file. Good practice always to close the file after opening it.
file_1.close()

# default mode
file_2 = open("harry.txt", "rt")  # read and text mode that is default mode
content_2 = file_2.read()
print(content_2)

file_2.close
# binary mode
file_3 = open("harry.txt", "rb")  # binary mode
content_3 = file_3.read()
print(content_3)

file_3.close

# reading some content of the document only
file_3 = open("harry.txt", "rt")
# will read the first 3 characters of the text file.
content_3 = file_3.read(3)
print(content_3)
# will read the next 3 characters of the text file. If all the characters are prviously read then this statement will return nothing
content_3 = file_3.read(3)
print(content_3)

file_3.close


# reading line by line in the file
file_4 = open("harry.txt")

for line in file_4:
    # this will print each line at each iteration with newline character as nill
    print(line, end="")

file_4.close()

# readline function
file_5 = open("harry.txt")

# read the first line of the file with \n (newline character) and than pointer will move to the next line.
print(file_5.readline())
# read the next line of the file with newline character and than pointer will move to the next line.
print(file_5.readline())
# read the next line of the file with newline character and than pointer will move to the next line.
print(file_5.readline())

file_5.close()

# reading a line character by character
file_6 = open("harry.txt")
content_6 = file_6.read()

for character in content_6:
    # this will print each character at each iteration with newline character as \n
    print(character)

file_6.close()

# readlines() function- to read the lines in the file and storing them in a list
file_7 = open("harry.txt")

print(file_7.readlines())

file_7.close()
