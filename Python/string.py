name = "Rohit Sharma"

# slicing
print(name[2:5])


# FORMATTING  :- dynamic string, writing string and variables together 
a=5
b=10
sum = a+b
## 1.format() (Introduced in python 3)

## normal formatting
# print("Sum of {} & {} is {}".format(a,b,sum))

## indexed based
# print("Sum of {1} & {0} is {2}".format(a,b,sum))

# # value based
# print("Values of variables are {a} & {b} ".format(a=2,b=4))


## 2. F-strings

print(f"Sum of {a} & {b} is {a+b}")