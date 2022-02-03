
# string to list
a = "spam"
b = list(a)
print(b)


a = "spam spam spam"
b = a.split()
print(b)

a = "spam-spam-spam"
b = a.split('-')
print(b)


# list to string
a = ['Hello', 'World']
b = " ".join(a)
print(b) # Hello World

# .sort() / sorted()
a = [1, 2, 3, 0]
print(a)
a.sort(reverse = False) # change a, return None 
b = sorted(a, reverse = False)
print(a)
print(b)


# .reverse() / reversed()
a = [1, 2, 3, 0]
print(a)
a.reverse() # change a, return None 
b = reversed(a)
print(a)
print(b)


# copy by value
import copy
b = copy.deepcopy(a)
b = a[:]
