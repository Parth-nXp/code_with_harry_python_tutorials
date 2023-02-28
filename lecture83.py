'''
Pickle module: The pickle module in Python is used for object serialization and deserialization. 
It allows you to convert any Python object (such as lists, dictionaries, classes, functions, etc.) into a stream of bytes that can be saved to a file or sent over a network. 
The pickled object can later be unpickled to its original form, which is useful for tasks such as saving and loading data or sending data between processes.

The pickle module provides two main methods: dump() and load(). 
The dump() method serializes an object and writes it to a file-like object, while the load() method reads a serialized object from a file-like object and returns the corresponding Python object.

Note that the pickle module is not secure and should not be used to deserialize untrusted data from an untrusted source, as it can execute arbitrary code.
'''

import pickle

# Pickling a python object
cars = ["Audi", "BMW", "Maruit Suzuki", "Harryti Tuzuki"]
file = "mycar.pkl"
fileobj = open(file, 'wb') # for pickling we use the binary file format instead of text mode
fileobj.close()


# to read the pickled object or to use it again in our code
file = 'mycar.pkl'
fileobj2 = open(file,'rb')
my_car = pickle.load(fileobj2)
print(my_car)
print(type(my_car)) # even the type of the object is also preserved while pickling