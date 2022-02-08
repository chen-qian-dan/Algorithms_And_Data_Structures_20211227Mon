print("Create -------------------------- ")
t = ('a', 'b', 'c', 'd', 'e')
print(t)

print("Access -------------------------- ")
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])
print(t[-1])

print("Slice -------------------------- ")
t = ('a', 'b', 'c', 'd', 'e')
print(t[0:3])


print("traverse -------------------------- ") # time: O(n), space: O(1)
t = ('a', 'b', 'c', 'd', 'e')
for v in t:
    print(v)

for i in range(len(t)):
    print(t[i])

for i, v in enumerate(t):
    print((i, v))


print("search -------------------------- ") # time: O(n)
t = ('a', 'b', 'c', 'd', 'e')
if 'a' in t:
    print(True)


print("index -------------------------- ")
t = ('a', 'b', 'c', 'd', 'e')
print(t.index('a'))
# print(t.index("no exist")) # ValueError


print("+ -------------------------- ")
t = ('a', 'b')
p = ('c', 'd')
tup = t + p
print(tup)

print("* -------------------------- ")
t = ('a', 'b')
tup = t * 2
print(tup)

print("count -------------------------- ")
t = ('a', 'b')
print(t.count('a'))

print("sorted -------------------------- ")
t = ('c', 'b')
newT = sorted(t)
print(newT)


print("min, max, sum -------------------------- ")
t = (1, 2)
print(min(t))
print(max(t))
print(sum(t))

print("list to tuple -------------------------- ")
t = tuple([1, 2])

print("tuple to list -------------------------- ")
lst = list((1, 2))
print(lst)


lst = [1, 2]
lst.reverse() # change itself
a = reversed(lst) # note: a is not a list, it is a list_reverseiterator
print(list(a)) # now, list(a) is a list 






