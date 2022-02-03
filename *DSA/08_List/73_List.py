from typing import List

lst: List[int] = list()
lst = [1, 2, 3]

def access(lst, index: int):
    if index >= len(lst):
        return "Index is out of range"
    return lst[index]



def traverse(lst):
    for i in lst:
        print(i)


lst = [1, 2]
lst.insert(8, 3)
print(lst)
# del lst[10]
print(lst)

a = lst.remove(1)
print(lst)
print(a)


# search
if 1 in lst:
    print(True)
for i, v in enumerate(lst):
    if v == 1:
        print(i)