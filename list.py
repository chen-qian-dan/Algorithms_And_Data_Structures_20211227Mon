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

# append
lst = ['Milk', 'Cheese', 'Butter']
lst.append('3')
print(lst)

# extend
lst = ['Milk', 'Cheese', 'Butter']
lst.extend([1, 2, 3])
print(lst)

# slice
lst = ['a', 'b', 'c', 'd', 'e']
print(lst[:2])
print(lst[2:])
print(lst[2:3]) # note: not the same as lst[2], lst[2] is an item, lst[2:3] is a list
print(lst[-1])
print(lst[:])
print(lst[:-2]) # the last 2 is the first not want


# pop
lst = ['a', 'b', 'c', 'd', 'e']
a = lst.pop()  # delete the last one
print(a)
print(lst)

lst = ['a', 'b', 'c', 'd', 'e']
a = lst.pop(0)  # delete the first one
print(a)
print(lst)

lst = ['a', 'b', 'c', 'd', 'e']
# a = lst.pop(0:3)  # no such thing


# delete
lst = ['a', 'b', 'c', 'd', 'e']
del lst[2]
print(lst)

lst = ['a', 'b', 'c', 'd', 'e']
del lst[0:2] # compare with pop, del return nothing
print(lst)


# remove
lst = ['a', 'b', 'c', 'd', 'e', 'e']
lst.remove('e') # only remove one 'e'
print(lst)

# search
if 20 in lst:
    print('True')
else:
    print('False')

def searchInList(lst, target):
    for i, v in enumerate(lst):
        if v == target:
            return i
    return 'Target is no in the list'

print(searchInList(lst, 'a'))