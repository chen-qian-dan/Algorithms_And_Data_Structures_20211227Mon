"""
create
insert / update 
traverse
search
delete / remove 
"""

d = dict()
print(d)
d[0] = 'a'
d[1] = 'b'
d[0] = 'c'
d['Hello'] = 'world'

for v in d.items():
    print(v)

print(len(d))
print(d.pop(0)) # return only value 
# print(d.popitem()) # delete a random pair 
print(d)
# d.clear 
# print(type(d))

del d['Hello'] # return None 



print("\n .copy() by value --------------------- ")
d = {1: 1, 2: 2}
newD = d.copy() # copy by value 


print("\n .fromkeys([keys], value) --------------------- ")
newD = dict().fromkeys([1, 2, 3], [0, 4, 5])
print(newD)

newD = dict().fromkeys([1, 2, 3])
print(newD)


print("\n .get(k, v) --------------------- ")
# return v is k is not found 
d = {1: 1, 2: 2}
print(d.get('H', 100))


print("\n .items() --------------------- ")
d = {1: 1, 2: 2}
print(d.items())


print("\n .keys() --------------------- ")
d = {1: 1, 2: 2}
print(d.keys())


print("\n .values() --------------------- ")
d = {1: 1, 2: 2}
print(d.values())


print("\n .popitem() --------------------- ")
# # delete a random pair 
d = {1: 1, 2: 2}
print(d.popitem())


print("\n .setdefault(key, defaultValue) --------------------- ")
# if key exists, return value, else add the key with the value 
d = {1: 1, 2: 2}
d.setdefault(3, 3)
print(d)


print("\n .pop(key, defaultValue) --------------------- ")
d = {1: 1, 2: 2}
print(d.pop(3, 3))
print(d)


print("\n .update(other_dictionary) --------------------- ")
d = {1: 1, 2: 2}
newDict = {'a': 1, 'b': 2, 'c': 3, 1: 40}
d.update(newDict)
print(d)



print("\n in operator --------------------- ") # time O(1)
d = {1: 1, 2: 2}
print(1 in d)
print(1 in d.keys())



print("\n for operator --------------------- ")
d = {1: 1, 2: 2}
for k in d.keys():
    print(k)

for k, v in d.items():
    print((k, v))



print("\n all operator --------------------- ")
"""
all values are true, return true 
empty iterable, return true 
others, return false 
"""
# ????????? why the output is different from expected ?
a = {}
print(all(a))

b = {1: True, 2: True}
print(all(b))

c = {1: True, 2: False}
print(all(c))

c = {1: False, 2: False}
print(all(c))

print("\n any operator --------------------- ")
"""
any(dictionary)
"""

a = {}
print(any(a))

b = {1: True, 2: True}
print(any(b))

c = {1: True, 2: False}
print(any(c))

c = {1: False, 2: False}
print(any(c))



print("\n len operator --------------------- ")
d = {1: 1, 2: 2}
print(len(d))

print("\n sorted() operator --------------------- ")
d = {3: 1, 2: 2}
a = sorted(d)
print(a)

a = sorted(d, reverse = True)
print(a)

d = {'3': 1, '2': 2}
a = sorted(d, key = len)
print(a)