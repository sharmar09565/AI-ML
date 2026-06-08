# List comprehensions:-  it simplifies the code. If we have to work on simple iterable and conditions then we use this

# # Let we have to store the square of the int 

# #Without list comprehensions

# sq = []

# for i in range(6):
#     sq.append(i*i)

# print(sq)


# #With list comprehensions

# square = [i*i for i in range(6)]
# print(square)


# # store the square of the even int 

# sq1 = [i*i for i in range(5) if i%2!=0] 
# print(sq1)


# # A list contains of +ve and -ve nums. We have to overwrite the list and replace the -ve nums to 0

# nums = [-3,1,5,-4,-1,3]

# nums = [0 if val<0 else val for val in nums]
# print(nums)


# We can also use function 

words = ["hello","hii","python"]

words = [val.upper() for val in words]
print(words)