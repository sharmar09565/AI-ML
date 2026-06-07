# Different FILE operations

#1 Reading a file('r')

# f = open("eg.txt","r")      # file object, read mode is default.

# # data = f.read()
# # print(data)
# # print(type(data))

# data = f.readline()     # read file line by line
# print(data)

# data = f.readline()     # to read next line repeat above code.
# print(data)


#2 Writing a file('w')

# f = open("eg.txt", "w")
# f.write("Rewrite the file")     #overwrite(truncate) the file 


#3 Appending at end('a')

# f = open("eg.txt", "a")
# f.write("\nA line is added")


# Creating and open for writing('x') :- a and w also creates file if it is not created but x is specially used when we have to create and write a file. If file is present in the folder the it throws an error 

# f = open("eg2.txt", "x")
# f.write("New file is created")


#4 Binary mode('b') - video, audio and images are opened in binary mode.


#5 Text mode('t') - file is treated as text. It is default. We can use multiple file mode together.
# Ex:- rt, wt, at, rb, wb, ab

#6 Open disk file for update(r & w)
# Ex:- r+ :- pointer is present at starting so its write/add the text from starting
#      w+ :- it rewrites the file
#      a+ :- pointer is present at end so its write/add the text from end

# f = open("eg.txt", "r+")
# f.write("123")
# print(f.read())

# f = open("eg.txt", "w+")
# f.write("123")
# print(f.read())

# f = open("eg.txt", "a+")
# f.write("123")
# print(f.read())

# f.close()



# with Keyword :- 
# it automatically close the file after operation. We don't have to close the file explicitly(i.e no need of f.close() after every operation)

# with open("eg.txt", "r") as f:
#     data = f.read()
#     print(len(data))


#  Delete files

import os

os.remove("eg2.txt") 