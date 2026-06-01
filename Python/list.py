# List :- it is a data structure in py that stores the data in a order and are mutable. It can stores different data types. Use [] brackets


# marks = [54,65,68,88,67]

# print(marks)
# print(len(marks))
# print(marks[3])

# # slicing
# print(marks[1:3])

# Methods
# li = [1,2,3,4,5,6,7]

# # 1.
# li.append(8)
# # print(li)

# #2
# li.insert(1,5)
# # print(li)

# #3.
# li.sort()
# # print(li)

# #4
# li.reverse()
# # print(li) 

# #5
# li.remove(5)
# print(li)


#  Loops in list

nums = [12,5,8,9,6,10]

# for el in nums:
#     print(el)

x = input("Find the el of list:")
x = int(x)
idx = 0
for el in nums:
    if(el==x):
        print(f"{x} is present at {idx}")
        break
    idx+=1
    if(idx==len(nums)-1):
        print(f"{x} is not present in the list.")