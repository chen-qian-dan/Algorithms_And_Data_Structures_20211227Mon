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
print(d['not exist key']) # KeyError: 'not exist key'