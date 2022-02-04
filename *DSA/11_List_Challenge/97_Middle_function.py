"""
Write a function called middle that takes a list and return a new list
that contains all but the first and last elements. 

myList = [1, 2, 3, 4]
middle(myList) # [2, 3]
"""

def middle(lst):
    if lst is None:
        return None 
    if len(lst) < 3:
        raise ValueError("len of list must >= 3")
    newLst = list(lst[1:-1])
    return newLst


myList = [1, 2, 3, 4]
newLst = middle(myList) # [2, 3]
print(newLst)
print(myList)