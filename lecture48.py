'''
Map filter & Reduce
Map: map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

'''

from re import A


numbers = ['3', '34', '64']

# to convert all the elements of the string to the integer

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])
# we can also perform this action using maps as

numbers = list(map(int, numbers)) # map(function you want to perform, iterable object on which you want to perform this function)
# Note: performing only map operation gives you a memory location, we actually need to convert it into a iterable object
print(map(int, numbers))
numbers[2] = numbers[2] + 1
print(numbers[2])

# you can also use a function to perform the map operation as

def square_of_numbers(numbers):
    return numbers*numbers

num_list = [2,3,5,6,76,3,3,2]
square_list = list(map(square_of_numbers,num_list))
print(square_list)

# or you can even use the lambda functions to perform the map operation

num_list = [2,3,5,6,76,3,3,2]
square_list = list(map(lambda x: x*x, num_list))
print(square_list)

# you can actually use the map function to perform a list of functions on any list as

def sq_list(a):
    return a*a

def cube_list(a):
    return a*a*a

func = [sq_list, cube_list]

for i in num_list:
    value = list(map(lambda x: x(i), func))
    print(value)

'''
filter function: The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
'''

lst = [1,2,3,4,5,6,7,8,9,10,11]

def is_greater_5(number):
    return number>5

greater_5 = list(filter(is_greater_5,lst)) # filter(function_name, iterable object) gives the output of the list which gives output true in function for the values from the iterable object

print(greater_5)

'''
Reduce: It is a part of the functools package/module. So you need to first import it.
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
'''
from functools import reduce
lst_2 = [1,2,3,4,5,6,7,8,9,10]
sum_list = reduce(lambda x,y:x+y,lst_2)
print(sum_list)



