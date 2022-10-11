'''
Anonymous/Lambda Functions : An anonymous function is a function that is defined without a name. 
This function is created using the lambda keyword, so it is also called lambda function
'''


# this is used to create a lambda/anonymous function for subtraction operator, which works as following function.
'minus = lambda x,y: x-y'
def minus(x, y): return x-y


print(minus(5, 6))


# program to sort the function in ascending order of 1st element (index from zero)
a = [[1, 14], [15, 6], [8, 23]]  # list of lists
# key takes a function as input to return how you want to sort the elements of a list.
a.sort(key=lambda x: x[1])
print(a)
