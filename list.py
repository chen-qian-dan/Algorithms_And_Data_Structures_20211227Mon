from typing import List

# create
lst = []
lst = List[int]
lst = [1, 2, 3]
lst = [None] * 10
lst = [[1, 2, 3], [4, 5], 6] 
# for row in lst:
#     for v in row:
#         print(v) # cannot do this because 6 is not iterable
print(lst)


# access
lst = ['Milk', 'Cheese', 'Butter']
print(lst[0])
# print(lst[3]) # IndexEror

# in
print('milk' in lst) # case sensitive

# lower
a = lst[0].lower()
print(a)

# traverse
for v in lst:
    print(v)

for i in range(len(lst)):
    print(lst[i])

for i, v in enumerate(lst):
    print(v)


# update 
lst = ['Milk', 'Cheese', 'Butter']
lst[0] = 'Egg'
print(lst)

# insert
lst = ['Milk', 'Cheese', 'Butter']
lst.insert(3, 1) # output: ['Milk', 'Cheese', 'Butter', 1]
print(lst)


