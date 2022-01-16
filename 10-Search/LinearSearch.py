# Linear Search

def linearSearch(lst, value) -> int:
    """
    return index if found, else return -1
    """
    for i, v in enumerate(lst):
        if v == value:
            return i 
    return -1 



lst = [1, 2, 3, 4, 5]
print(linearSearch(lst, 59))