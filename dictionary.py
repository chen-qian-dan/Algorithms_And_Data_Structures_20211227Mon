# create dictionary ----------------------
from typing import Dict 
d: Dict[int, str] = dict()
d = {}
d = {1: 'a', 2: 'b'}
d[3] = 'c'
print(d)

print(d.keys()) # output dict_keys([1, 2, 3])
print(d.values()) # output dict_values(['a', 'b', 'c'])

print(type(d.values())) # <class 'dict_values'>
# print(d['not exist key']) # KeyError: 'not exist key'


# Update ---------------------------------
d = {'name': 'Qian', 'age': 37}
d['age'] = 27
print(d['age'])

# add ---------------------------------
d['phone'] = '0404'
print(d)


# traverse ---------------------------------
print("traverse ---------------------------------")
for k in d.keys():
    print(k, d[k])

print("print d -----------------------------")
print(d)

print("in d: --------------------------------")
for k, v in enumerate(d):
    print(k, v)

# search -------------------------------------
print("search -------------------------------------")
target = 9

def searchDict(d, target):
    for k in d:
        if d[k] == target:
            print("True")
    print("False")

searchDict(d, target)


print("pop() ----------------------------------")
d = {'name': 'Qian', 'age': 37}
value = d.pop('name')
print(d)
print(value)



print("popitem() ----------------------------------")
d = {'name': 'Qian', 'age': 37}
value = d.popitem() # must be no argument return {k, value}, pop a random pair
print(d)
print(value)


print("clear() ----------------------------------")
d = {'name': 'Qian', 'age': 37}
d.clear()
print(d)


print("del ----------------------------------")
d = {'name': 'Qian', 'age': 37}
del d['name']
print(d)
del d

print("copy() ----------------------------------")
d = {'name': 'Qian', 'age': 37}
dd = d.copy() # by value
dd['name'] = 'Dan'
print(d)
print(dd)

dd = d # by ref
dd['name'] = 'Dan'
print(d)
print(dd)

print("fromkeys ----------------------------------")
d = {'name': 'Qian', 'age': 37}
newd = {}.fromkeys([1, 2, 3], 0)
print(newd)

print(".get{key, value} ----------------------------------")
d = {'name': 'Qian', 'age': 37}
print(d.get('gender', 'F'))

print(".items() ----------------------------------")
d = {'name': 'Qian', 'age': 37}
print(d.items()) # output: dict_items([('name', 'Qian'), ('age', 37)])

print(".keys() ----------------------------------")
d = {'name': 'Qian', 'age': 37}
print(d.keys())


print(".values() ----------------------------------")
d = {'name': 'Qian', 'age': 37}
print(d.values())


print(".setdefault(key, default_value) ----------------------------------")
d = {'name': 'Qian', 'age': 37}
print(d.setdefault('gender', 'M'))


# get vs setdefault
print("get vs setdefault ----------------------------------")
d = {}
a = d.setdefault('a', )
print(a, d)

d = {}
a = d.get('a', 1)
print(a, d)
