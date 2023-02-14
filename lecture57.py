'''
Class methods as alternative constructor
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
        parameters_from_str = str_to_class.split('-')
        return cls(parameters_from_str[0], parameters_from_str[1], parameters_from_str[2]) 
        # we can also use oneline code for this using the *args as
        # return cls(*str_to_class.split('-'))


harry = Employee('Harry', 45500,'Instructor')
rohan = Employee('Rohan', 4500, 'Student')
karan = Employee.from_str_to_class('Karan-12000-Student')


harry.change_no_of_leaves(10)

print(harry.no_of_leaves)
print(karan.__dict__)