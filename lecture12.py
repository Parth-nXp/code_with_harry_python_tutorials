'''
Sets 
'''

# Set is a collection of unique elements. it is unordered and does not allow duplicates.
s = set()
# set is created by using curly braces {} or set() function.
print(type(s))  # <class 'set'>

list = [1, 2, 3, 4, 5]  # creating a list
s_from_list = set(list)  # converting list to set
print(s_from_list)  # {1, 2, 3, 4, 5}

s.add(1)  # adding element to set
s.add(1)  # adding same element again will not add it again
s1 = s.union([2, 3, 4])  # union of two sets
s2 = s.intersection([2, 3, 4])  # intersection of two sets
print(s1, s2)  # {1, 2, 3, 4, 5} {2, 3, 4}
print(s1.isdisjoint(s2))  # False
# disjoint means no common elements
