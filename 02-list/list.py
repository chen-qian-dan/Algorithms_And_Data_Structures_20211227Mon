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


a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # [1, 2, 3, 4, 5, 6], concate
print(a * 2)
print(len(a))
print(a.count(1))
print(max(a))
print(min(a))
print(a, b)


for x, y in zip(a, b):
    print(x, y)

print(sum(a))
# print(sum(a, b)) # no such thing


import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)


# [::2]
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a)

# ------------------------------
a=[1,2,3,4,5]
print(a[3:0:-1]) # output: [4, 3, 2]




# ------------------------------
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1 # by ref
fruit_list3 = fruit_list1[:] # by value
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

for ls in (fruit_list1, fruit_list2, fruit_list3):
    print(ls)


for a in (1, 2, 3):
    print(a)



# ------------------------------
def f(i, values = []):
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)
"""
output:
[1]
[1, 2]
[1, 2, 3]
"""

