'''
    Lists data structures
'''

grocery = ['cleaner', 'Biscuits', 'Apples', 56]
print(grocery)  # print the list
print(grocery[0])  # print the first element of the list
print(grocery[-1])  # print the last element of the list
numbers = [2, 4, 6, 8, 10]
print(numbers[2:])  # print the list from index 2 to the end
numbers.sort()  # sort the list
numbers.reverse()  # reverse the list
'''
Slicing of the list
'''
print(numbers[:])  # print the list from index 0 to the end
print(numbers[::2])  # print every 2nd element of the list
print(numbers[::-1])  # print the list in reverse order
print(numbers[1:5:-2])  # print the list from index 1 to 5 and reverse the list
# negative slicing should never be used or else it will give unexpected results
print(len(numbers))  # print the numbers of elements in the list
print(max(numbers))  # prints the max value in the list
print(min(numbers))  # prints the min value in the list

numbers.append(7)  # adds elements into the list from the last
print(numbers)  # print the list
numbers.insert(2, 5)  # inserts elements into the list from the specified index
# in insert, the first argument is the index and the second argument is the element to be inserted
numbers.remove(5)  # removes the element from the list
numbers.pop()  # removes the last element from the list


'''
Tuples data structures
'''
numbers[1] = 98  # this inserts the element into the list at the specified index

# List are mutable, but tuples are immutable
# mutable means that the elements of the list can be changed
# immutable means that the elements of the list cannot be changed
# () are called parentheses
# [] are called brackets
# {} are called curly brackets

tp = (1, 2, 3, 4, 5)  # create a tuple, parentheses are used to create a tuple
print(tp)
# tp[1] = 98 # this will give an error because tuples are immutable


'''
Swap two elements with temp variable
'''
a = 1
b = 2
temp = a  # this is used to store the value of a in a temporary variable
a = b  # this is used to change the value of a to b
b = temp  # this is used to change the value of b to the value of a stored in temp

# temporary variables are used to store the value of a variable in a temporary variable


# or we can simply do this

a, b = b, a  # this is used to swap the values of a and b
