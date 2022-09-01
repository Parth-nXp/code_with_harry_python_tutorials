# Dictionary is a collection of key-value pairs.

d1 = {}  # create an empty dictionary
print(type(d1))  # print the type of the dictionary

# {} are used to create a dictionary
# () are used to create a tuple
# [] are used to create a list

d2 = {"Harry": "Burger", "Ron": "Pizza", "Hermione": "Pasta"}
# here first argument is the key and the second argument is the value
# Note: Python is case sensitive
# Keys must be unique but values can be repeated

print(d2)  # print the complete dictionary
print(d2["Harry"])  # print the value of the key Harry
print(d2.get("Harry"))  # print the value of the key Harry

# Dictionary can also be inserted into a dictionary and this is called nested dictionary

d3 = {"Harry": "Burger", "Ron": "Pizza", "Hermione": "Pasta", "Dumbledore": {
    "Breakfast": "Coffee", "Lunch": "Sandwich", "Dinner": "Pizza"}}  # nested dictionary
print(d3["Harry"])  # print the value of the key Harry
# print the value of the key Dumbledore at the key Breakfast
print(d3["Dumbledore"]["Breakfast"])
# keys are immutable so we cannot change the key but values can be changed and are mutable


'''
To add new key-value pair to the dictionary
'''

d3["albus"] = "Potter"  # add a new key-value pair to the dictionary
print(d3)  # print the complete dictionary
# add a new key-value pair to the dictionary and the key is an integer. So key can be any immutable type
d3[420] = "Nothing"

print(d3)  # print the complete dictionary
del d3[420]  # delete the key-value pair with the key 420
print(d3)  # print the complete dictionary
print(d3.copy())  # copy the dictionary

'''
Use of copy() method
'''

d4 = d3  # d4 is a copy of d3
# delete the key-value pair with the key Dumbledore not only from d4 but also from d3
del d4["Dumbledore"]

# to delete the key-value pair with the key Dumbledore from d4 but not from d3 use the method copy() like this


d4 = d3.copy()  # copy the dictionary
# delete the key-value pair with the key Harry only from d4 and not from d3 since d4 is a copy of d3
del d4["Harry"]


'''
functions of dictionary
'''

print(d2.get("Harry"))  # get the value of the key Harry
# update the dictionary with a new key-value pair
d2.update({"Luna": "Toffee"})
print(d2)  # print the complete dictionary
print(d2.keys())  # print the keys of the dictionary
print(d2.items())  # print the key-value pairs of the dictionary
