'''
Comprehensions: Comprehensions are a concise way to create sequences (like lists, sets, or dictionaries) in Python. 
They allow you to specify the elements of a sequence using a compact and readable syntax.
There are three types of comprehensions in Python:
1. List comprehensions: used to create lists based on an iterable, with an optional filtering condition.

2. Set comprehensions: used to create sets based on an iterable, with an optional filtering condition.

3. Dictionary comprehensions: used to create dictionaries based on an iterable, with an optional filtering condition.
'''

l = []
for i in range(100):
    if i % 3==0:
        l.append(i)

print(l)

# we can also perform this in one line using list comprehensions as
ls = [i for i in range(69) if i % 3==0] # this is list comprehension
print(ls)

# {0: "item0", 1: "item1", 2: "item2" and so on...} we can use dictionary comprehension
dict1 = { i:f"item{i}" for i in range(1,1000+1) if i%100==0}
print(dict1)

# To reverese any dictionary we can actually use a dictionary comprehension
dict2 = { i:f"Item{i}" for i in range(5) }
dict3 = {value:key for key,value in dict2.items()}
print(dict2,"\n" ,dict3)


# set comprehension
dresses = {dress for dress in ['dresses1', 'dresses2', 'dresses3','dresses1', 'dresses2', 'dresses3', 'dresses1', 'dresses2', 'dresses3']} # set comprehension {}, list comprehension []
print(dresses)
print(type(dresses))

# Generator comprehension: Generator comprehensions, also called generator expressions, are similar to list comprehensions but instead of creating a list, they create a generator object.
# A generator comprehension is created using parentheses () instead of square brackets [], and the elements are generated lazily as requested. 
# This can be more memory-efficient than creating a list, as only one element is generated at a time. 
# Generator comprehensions can be a useful tool for generating large sequences of data on-the-fly, without the need to store them all in memory at once.

evens = (i for i in range(100) if i%2==0)
print(type(evens))
for item in evens:
    print(evens.__next__())
