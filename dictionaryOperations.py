
print("\n in ----------------------------------")
d = {'name': 'Qian', 'age': 37}
if 'name' in d: # in keys()
    print("True")

for k, v in enumerate(d): # index, keys
    print(k, v)


print("\n all ----------------------------------")
d = {1: True, 0: False}
print(all(d))

d = {0: False, 1: False}
print(all(d))



print("\n any ----------------------------------")
d = {1: True, 0: False}
print(any(d))

d = {0: False, 1: False}
print(any(d))


print("\n len ----------------------------------")
d = {1: True, 0: False}
print(len(d))

