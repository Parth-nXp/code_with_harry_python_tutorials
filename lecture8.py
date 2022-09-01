mystr = "harry is a good boy"
print(mystr)
print(mystr[4])  # indexing in python starts from 0
print(mystr[5])
print(mystr[0:9])  # all string letters from 0 to 9 where 9 not excluded
print(len(mystr))  # print the number of characters in a string

print(mystr[0:9:2])  # print every 2nd character
print(mystr[:9])  # print everything from 0 to 8
print(mystr[0:])  # print everything from 0 to the end
print(mystr[::])  # print everything

'''
Negaive indexing
'''

# print from -4 to -2 where -2 not included and -4 is included.
print(mystr[-4:-2])
# -ve indexing starts from the end of the string

print(mystr[-1])  # print the last character
print(mystr[::-1])  # print the string in reverse order
print(mystr[::-2])  # print every 2nd character in reverse order


'''
Methods of string
'''

print(mystr.isalnum())  # check if the string is alphanumeric or not
# space is not considered as alphanumeric
print(mystr.isalpha())  # check if the string is alphabetic or not
# space is not considered as alphabetic
# endswith checks if string ends with the string entered in the function
print(mystr.endswith("boy"))
print(mystr.count("o"))  # counts the number of o in our string
print(mystr.capitalize())  # capitalize the first letter of the string
print(mystr.find("is"))  # finds the location of the is in terms of indexing
print(mystr.replace("is", "was"))  # replace the is with was
print(mystr.lower())  # convert the string to lower case
print(mystr.upper())  # convert the string to upper case
