'''
Writing and Appending to a File
'''
# creating a new text tile

file = open("Harry2.txt", "w")  # creating new file in writing mode
file.write("Harry bhai bahut ache hai")  # writing in the file
file.close()  # good practice to always close the file after use
# Note- If file already exist it will delete all the content of that file and will update it with new content.
# if you want to add content to the same file you need to open that file in append mode

# append mode in text file

file_2 = open("Harry2.txt", "a")  # opening the file in append mode
file_2.write("\nHarry is a good boy")  # writing(appending) in the file
file_2.close()  # closing the file


# to find how many characters we have inserted into the file

file_3 = open("Harry2.txt", "a")
# counting how many characters we have written, works for both write and append mode
a = file_3.write("\nHarry is a good boy")
file_3.close()  # closing the file
print(a)


# to open file in both read and write mode
# r+ specifies that we want to open the file in both read and write mode
file_4 = open("Harry2.txt", "r+")
# first it will read all the content of the file and then it will print it.
print(file_4.read())
file_4.write("\nThank you")  # writing in the file
file_4.close()
