'''
Enumerate function: Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
This enumerated object can then be used directly for loops or converted into a list of tuples using the list()
'''

l1 = ['Bhindi', 'Aloo', 'chopsticks', 'chowmein']

for index, item in enumerate(l1): # enumerate gives access to two attributes of the list: index and value. 
    # Note that the index value always starts with 0.
    if index%2==0:
        print(f'Jarvis please buy {item}')
    