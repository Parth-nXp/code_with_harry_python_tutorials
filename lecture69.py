'''
Setter: a setter is a method that is used to set the value of an instance variable of a class. 
It is usually defined as part of a property, which is a way of controlling access to instance variables of a class.
Using a property with a setter allows you to enforce constraints on the values that are assigned to an instance variable, such as ensuring that they are of a certain type or within a certain range. 
It also provides a way to execute additional logic whenever a value is assigned to the variable, such as updating other related variables or triggering other actions.

Property Decorator: the property decorator is a built-in function that allows you to define getter, setter, and deleter methods for an instance variable of a class, but access the variable as if it were a normal instance variable.

Deleter Decorator: In Python, the @property decorator provides a way to define getter methods for instance variables, and the @property_name.setter decorator provides a way to define setter methods for those variables. 
The @property_name.deleter decorator provides a way to define a method that will be called when the property is deleted using the del keyword.
The @property_name.deleter decorator is useful when you want to perform some action when a property is deleted, such as freeing up resources that are associated with the property.
'''

class Employeee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email =  f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property # using this property decorator we dont need to call self.email() method instead we can call it directly as a property self.email
    def email(self):
        if self.fname == 'None' and self.lname == 'None':
            return "Email is not set. Please set it using setter."
        return f"{self.fname}.{self.lname}@codewithharry.com"
    
    # now suppose we wan to change the first name and the last name after changing the email. we can use the setter as
    @email.setter
    def email(self,string):
        print('Setting now...')
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    # to delete any attribute we generally use the del attribute. Suppose we want ot deleter the email attibute, we generally dont delter the attribute else we just set it to none as
    @email.deleter
    def email(self):
        self.fname = 'None'
        self.lname = 'None'
        #after this we will create if condition in the email function

    
hindustani_supporter = Employeee('Hindustani', 'Supporter')
nikhil_raj_pandey = Employeee('Nikhil', 'Raj Pandey')

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"
print(hindustani_supporter.email)
# Even after changing the fname the email id will not change. This problem is solved in python using the setter

## now to chage the fname and lname using the email we can use setter so,
hindustani_supporter.email = 'this.that@codewithharry.com'
print(hindustani_supporter.fname)

# now delete the email and then check it
del hindustani_supporter.email
print(hindustani_supporter.email)