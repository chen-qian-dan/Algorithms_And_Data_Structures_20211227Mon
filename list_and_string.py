from typing import List
# string to list
a: str = 'spam'
b: List[str] = list(a)
print(b)


a: str = 'spam spam spam'
b: List[str] = a.split()
print(b)

a: str = 'spam-spam1-spam2'
b: List[str] = a.split('-')
print(b)

# join
print('_'.join(b))


# sort
lst: List[int] = [2, 4, 3, 1, 5, 7]
lst.sort()
print(lst)
lst.sort(reverse = True)
print(lst)

lst: List[int] = [2, 4, 3, 1, 5, 7]
newlst = sorted(lst)
print(newlst)
newlst = sorted(lst, reverse=True)
print(newlst)
