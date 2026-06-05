# Dictionary :- stores the value in key:pairs. This is mutable and unordered

#Note:- key is always unique, key can be if any data types

info = {
    "name": "Rohit",
    "age": 21,
    "marks": 85

}
print(type(info))
print(info["name"])

# Methods

#1 dict.keys() 

print(type(info.keys()))
print(list(info.keys()))

#2 dict.values()

#3 dict.items()    returns all key value pairs

#4 dict.get(key)  returns value of the key
 
#5 dict.update(new_item)    add new item to dict

info.update({
    "weight": 50
})