tup = (1, 2, 3)
print(tup)




print("tuple with one item ---------------------")
# tuple with only one element, must with ,
tup = ('a') # a string
print(type(tup))

tup = ('a',) # a tuple
print(type(tup))

tup = tuple() # create an empty tuple
print(type(tup))

tup = tuple('abc') 
print(tup) # output: ('a', 'b', 'c')


print("\n access ----------------------------------")
tup = (1, 2, 3, 4)
print(tup[0])
print(tup[-1])
print(tup[0:2]) # output: (1, 2)

print(tup[::-1]) # output: (4, 3, 2, 1)

print(sorted(tup)) # [1, 2, 3, 4]

print(min(tup))

print("\n traverse ----------------------------------")
tup = (1, 2, 3, 4)
for v in tup:
    print(v)

for i in range(len(tup)):
    print(tup[i])

for i, v in enumerate(tup):
    print(i, v)


print("\n search ----------------------------------")
tup = (1, 2, 3, 4)
if 'b' in tup:
    print(True)
else:
    print(False)


print("\n concate ----------------------------------")
tup1 = (1, 4, 3, 2, 5)
tup2 = (1, 2, 6, 9, 8, 7)
print(tup1 + tup2) # (1, 4, 3, 2, 5, 1, 2, 6, 9, 8, 7)

print(tup1 * 2) # (1, 4, 3, 2, 5, 1, 4, 3, 2, 5)

print("\n in ----------------------------------")
tup1 = (1, 4, 3, 2, 5)
print(1 in tup1)
