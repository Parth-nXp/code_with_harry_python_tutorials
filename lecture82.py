'''
JSON module: The json module in Python provides an easy way to encode and decode data in JSON (JavaScript Object Notation) format. 
It provides two methods: json.dumps() and json.loads().

json.dumps() is used to encode a Python object into a JSON-formatted string. The method takes a Python object as input and returns a string.

json.loads() is used to decode a JSON-formatted string into a Python object. The method takes a JSON-formatted string as input and returns a Python object.
'''

import json

# json is always written in double quotes. commenting is avoided while making json
data = '{"var1" : "Harry", "var2" : 56}' 
# to make data parse so that we can directly access the value from the key we use json.loads(). It usually creates dictionary from string
parsed = json.loads(data)
print(parsed['var1'])
print(type(parsed))

data2 = {
    "CodeName": "CodeWithHarry",
    "cars": ["BMW", "audi", "Ferrari"],
    "ferrari":('roti', 540)
}

# to make data2 javascript compatible we use json.dumps as
jscomp = json.dumps(data2)
print(jscomp)