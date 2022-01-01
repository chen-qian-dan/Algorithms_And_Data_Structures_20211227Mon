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