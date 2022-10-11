'''
Using Python External & Built In Modules
'''

import random  # this is how we import the built in modules. We can check the modules via clicking ctrl+right click on module


# to generate random number between 0 and 5
random_integer = random.randint(0, 5)
print(random_integer)


# to generate random number between 0 and 1
random_number = random.random()
print(random_number)

# to choose an element randomly from a list
lst = ['Star Plus', 'DD1', 'Aaj Tak', 'CodeWithHarry']
choice = random.choice(lst)
print(choice)

# to install any module run this in terminal pip install module_name
