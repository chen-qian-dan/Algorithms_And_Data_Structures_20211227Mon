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


print('_'.join(b))