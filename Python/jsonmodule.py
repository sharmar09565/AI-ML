# JSON module:-
    # json.loads()
    # json.dumps()
    # json.load()
    # json.dump()
# load- convert json into py obj
# dump- convert py obj into json
# s in loads and jumps is string. 

# loads and jumps are used when data is in string format

# load and jump is used when data is present in a file


import json

# #1. json.loads()

# json_str = '{"name": "Rohit", "age": 20,"eligible": true, "working": null}'   # data in json string format

# py_obj = json.loads(json_str)  # converting json string into py object(i.e dictionary)

# print(type(py_obj), py_obj)


# #2. json.dumps()

# py_object = {
#     "name": "Rohit",
#     "age": 20,
#     "eligible": True,
#     "working": None
# }

# json_string = json.dumps(py_object)

# print(type(json_string), json_string) 


# #3 json.load()

# with open("data.json", "r") as f:
#     py_ob = json.load(f)
#     print(py_ob)


#4 json.dump()

data = {
    "name": "Rohit",
    "age": 20,
    "eligible": True,
    "working": None 
}

with open("data.json", "w") as f:
    json_data = json.dump(data, f, indent=4, sort_keys=True)

# ident is used write the data in a format document. We can skip this but json data will show in a single line.

# sort_keys sort the data

# These are extra things used in this 