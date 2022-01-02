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