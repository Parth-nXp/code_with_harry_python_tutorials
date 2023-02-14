'''
Multiple Inheritance: Multiple inheritance is a feature of object-oriented programming in which a derived class can inherit attributes and methods from two or more base classes. 
In other words, a derived class can have multiple parent or base classes.
Multiple inheritance can be a powerful and flexible way to reuse code and create complex class hierarchies, but it can also make code harder to read and understand, and can lead to conflicts and ambiguities if the same attribute or method is defined in multiple base classes. 
Therefore, it should be used with care and with a good understanding of its potential advantages and pitfalls.
'''

class Employee:
    no_of_leaves = 8 

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def __init__(self, name_argument, salary_argument, role_argument): # this is how we create a constructor
        self.name = name_argument
        self.salary = salary_argument
        self.role = role_argument

    @classmethod
    def change_no_of_leaves(cls, new_no_of_leaves):
        cls.no_of_leaves = new_no_of_leaves

# below class method takes a string and return an instance in class Employee, such that it splits the string and creates value of different instance variable
    @classmethod
    def from_str_to_class(cls, str_to_class):
        return cls(*str_to_class.split('-'))

# below method is used to create a static method. The reason we defined it in class and not outside class is because sometimes we need some methods to be executed only for the objects and not for any other variable.
    @staticmethod
    def printgood_method(string_as_input):
        print("This is good "+ string_as_input)

class Player():
    no_of_games = 4

    def __init__(self, name_argument, game_argument):
        self.name = name_argument
        self.game = game_argument


    def print_details(self):
        return f'The name of Player is {self.name}. The game played is {self.game}'

    @classmethod
    def split_strin_for_class(cls, string_as_input):
        return cls(*string_as_input.split('-'))


class cool_programmer(Employee,Player):
    pass


harry = Employee('Harry', 45500,'Instructor')
rohan = Employee('Rohan', 4500, 'Student')


shubham = Player.split_strin_for_class('Shubham-Tennis')
karan = cool_programmer.from_str_to_class('Karan-250000-Cool Programmer')
print(karan.__dict__)