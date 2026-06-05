l = [
    ("Alice", "Maths"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Maths"),
    ("Bob", "Maths"),
    ("Alice", "English"),
    ("Charlie", "English")
]

# Q1. list all unique courses

sub = set()

# for el in l:
#     sub.add(el[1])

# without using idx
for name, course in l:
    sub.add(course)

print(sub) 

# Q2. list students enrolled in english

eng_std = set()

for name, course in l:
    if (course == "English"):
        eng_std.add(name)

print(eng_std)

#3  create dict(std, set of course)

dict = {}
for name, course in l:
    if(dict.get(name)==None):
        dict.update({name: set()})   # if name is already present in dict
    dict[name].add(course)          # add current course

print(dict)