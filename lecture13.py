'''
If - Else statement
'''

var1 = 100  # integer
var2 = 200  # integer

var3 = int(input("Enter a number: "))  # string converted to integer


if var3 > var2:  # this is a condition whose result is boolean
    # if condition is true, : means do this
    # spaces in starting is important and called indentation.
    print("var3 is greater than var2")
    # this statement will be executed if the condition is true
elif var3 == var2:  # elif is another condition which is true if the previous condition is false and means else if
    # == means equal to , != means not equal to, > means greater than, < means less than, >= means greater than or equal to, <= means less than or equal to
    # = is used to assign value to a variable and == is used to compare the value of a variable
    # this statement will be executed if the new condition is true and the previous condition is false
    print("var3 is equal to var2")
else:  # this statement will be executed if the condition is false
    print("var3 is less than var2")


'''
If - Else statement with in operator, and, or, not
'''

list1 = [1, 2, 3, 4, 5, 6, 7]  # list
if 5 in list1:  # this is a condition whose result is boolean
    # in operator checks if the value is in the list
    print("5 is in list1")
    # this statement will be executed if the condition is true

if 15 not in list1:  # not in operator checks if the value is not in the list
    print("15 is not in list1")
    # this statement will be executed if the condition is true


'''
Quiz
'''
age = int(input("Enter your age: "))

if age > 18:
    print("You are able to drive")
elif age < 18:
    print("You are not able to drive")
else:
    print("We cant decide, go for physical verification")


'''
Quiz 2
'''

age = int(input("Enter your age: "))

if age >= 7 and age <= 100:  # and operator checks if both conditions are true
    # or operator checks if either of the conditions are true
    # not operator checks if the condition is false
    if age > 18:
        print("You are able to drive")
    elif age < 18:
        print("You are not able to drive")
    else:
        print("We cant decide, go for physical verification")
else:
    print("This is not a valid age")
