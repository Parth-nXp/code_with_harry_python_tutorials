

'''
# For loops
'''
# for loops are used to iterate over a sequence of items, such as a string, a list, a tuple, a dictionary, a set, or a file.
# they are used to execute a set of statements a certain number of times.
# it is useful when you have a definite number of times you want to repeat a set of statements.
list1 = ["Harry", "Ron", "Hermione", "Ginny", "Dobby"]

for item in list1:  # for each item in list1, execute the following code
    print(item)    # print the item

# for loops can also iterate over a tuple, a dictionary, and a file but should be avoided on a string and a set.

# for loops on tuples

list2 = ("Harry", "Ron", "Hermione", "Ginny", "Dobby")

for item in list2:  # for each item in list2, execute the following code
    print(item)  # print the item

# for loops on list of lists

list3 = [["Harry", 1], ["Ron", 2], ["Hermione", 3], ["Ginny", 4], ["Dobby", 5]]

for item, lollypop in list3:  # for each item and lollypop in list3, execute the following code
    print(item, "and lolly is", lollypop)  # print the item and lollypop


dict1 = dict(list3)  # convert list3 to a dictionary
print(dict1)
'''
# for item, lollypop in dict1: #  this will give an error because dict1 is a dictionary and not a list
#    print(item, "and lolly is", lollypop)
'''
# for iterating over a dictionary use the following:
for item, lollypop in dict1.items():  # for each item and lollypop in dict1, execute the following code
    print(item, "and lolly is", lollypop)  # print the item and lollypop

# to print the keys of a dictionary use the following:
for item in dict1:  # for each item in dict1, execute the following code
    print(item)  # print the item


'''
create a random list of any datatype and check if item is number or not and if it is grater than 6 then print that number
'''
random_list = ["Hello", "list", 62, 7.32, True, [1, 2, 3],
               {"key": "value"}, (1, 2, 3)]  # create a random list

for item in random_list:
    if isinstance(item, int) or isinstance(item, float):
        if item >= 6:
            print(item)


# or you can use the following:

for item in random_list:
    # str(item).isnumeric() converts item to a string and then checks if it is numeric
    if str(item).isnumeric() and item > 6:
        print(item)
