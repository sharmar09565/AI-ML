# Tuple :- it is immutable data type

# tup = (1,2,3,4,"we")
# tup1 = (5)      # type of tup1 here will be num as it stores single value element without comma.
# tup2 = (5,)     # it's type will be Tuple as el is separated by comma


# Methods

#  same slicing and loops in tuple is used as list

# t = (5,6,8)
# sum=0
# for el in t:
#     sum+=el
# print(sum)


t = (1,2,4,2,3,5,2,3)

#1 t.index(val) - it returns first occurrence of el in tup

print(t.index(2))

#2 t.count(val)

c = t.count(2)
print(c)