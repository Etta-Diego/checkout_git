# Json Javascript Object Notation is a format for structuring data. 
# It is mainly used for storing and transferring data between the browser and the server.

# json.loads() converts json string into a python dictionary

import json

# JSOn string
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(employee))

print("\nNow convert from JSON to Python")

# Convert string to Python dict
employee_dict = json.loads(employee)
print("Converted to Python", type(employee_dict))
print(employee_dict)


# JSON string
employee_dict = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
print("This is Python", type(employee_dict))

print("\nNow convert from python to JSON")

# Convert Python dict to Json
json_object = json.dumps(employee_dict, indent=4)
print("Converted to JSON", type(json_object))
print(json_object)


# There are 6 Json data types
# String    \
# Number      \
#              > Simple data types
# Boolean     /
# Null       /

# Object \
#         / >   Complex data types
# Array  / 


# Json string must be written in double quotes
        #   {"name": "Ikenna"}

# Json Number is represented in base 10, not in octal and hexadecimal formats
        # {"age": 20}

# Json boolean can either be true or false
        # {"result": true}

# Json Null defines a nullable value
        # {
        # "result" : true,
        # "grade" : null
        # "regno" : 127
        #}

# Json object is a set of name of value pairs inserted between curly braces.
    # The keys must be strings, be unique, and separated by a comma.
        # {
        # "Geek":{"name": "Peter", "age:20, "score": 65}
        # }


# Json Array is an ordered collectionof values inserted between a square brackets
        #{
        # "student_names": ["Hannah", "Fiona", "Taminu"]
        #}

"""
Json supports different primitive types
Conversion from python object to json object as follows:
"""   

# list conversion to Array
print(json.dumps(['Welcome', "to", "Nigeria"]))

# tuple conversion to Array
print(json.dumps(("Welcome", "to", "Nigeria")))

# String conversion to string
print(json.dumps("Hello"))

# int conversion to Number
print(json.dumps(4578))

# float conversion to Number
print(json.dumps(5678.86))

# Boolean conversion to bool
print(json.dumps(True))
print(json.dumps(False))

# None value to null
print(json.dumps(None))

"""
Serializing Json is the process of converting a data structure or object state into a format that can be easily stored and transmitted
Python objects like dict, list and array, str, int long and float, True, False, None are converted into Json object as object, 
array, string, numbers, true, false, null respectively.

"""
var = {
    "Subjects": {
        "Maths":85,
        "Physics":90
    }
}


with open("Sample.json", "w") as p:
    json.dump(var, p)

"""
Deserialization is the conversion of JSON objects into their respective Python objects using load() method
"""

with open("Sample.json", "r") as f:
    read = json.load(f)


import demjson

"""
Encoding is defined as converting the text or values into an encrypted form that can only be used by the desired user through decoding it.
The encode() function is used to convert the python object into a JSON string representation.
"""

# Storing marks of 3 subjects

var = [{"Math": 50, "Physics": 60, "Chemistry": 70}]
print(demjson.encode(var))


# The decode() function is used to convert the JSON object into python format type

variable = '{"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}'
text = demjson.decode(variable)
print(text)


# Encoding is the process of onverting the text or values into an encrypted form that can only be used by the 
# desired user through decoding it. 
# Encoding and serialization are used interchangeablely, however, they have little difference.
# Serialization refers to the process of converting a Python data structure (like a list or dictionary) into a JSON string. 
# The main goal is to convert the object into a format that can be easily stored or transmitted.
# Serialization typically involves both encoding (converting data into a specific format) and
#  any additional steps needed to make the data suitable for storage or transmission.


# Iterencode allows you to convert the data into JSON one small piece at a time, just like sending the book chapter by chapter.
#  This process is called incremental encoding.

json.JSONEncoder().encode({"foo": ["bar"]})
'{"foo"}: ["bar"]}'

for i in json.JSONEncoder().iterencode(bigobject):
    print(mysocket.write(i))


# Demjson  is a third-party library that provides more flexibility and 
# features for working with JSON data compared to the standard json module.
# It can be useful when you need additional capabilities.