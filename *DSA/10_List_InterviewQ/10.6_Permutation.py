"""
check for two given two lists, if they are permutation to each other
permutation: same items, different / same order

exam:
[1, 2] and [2, 1] is permutation to each other
[1, 2] and [2, 1, 1] is not

1. problem
2. input
3. output
4. edge cases
5. time
6. space 
"""

def isPermutation(lst1, lst2) -> bool:
    if len(lst1) != len(lst2):
        return False 
    if len(lst1) == 0:
        return True 

    # count lst1 to a dict
    counter = dict()
    for v in lst1:
        if v in counter.keys():
            counter[v] += 1
        else:
            counter[v] = 1

    # check lst2
    for v in lst2:
        if v in counter.keys():
            counter[v] -= 1
        else:
            return False 
    if sum(counter.values()) > 0:
        return False 
    return True


lst1 = ['a', 'c', 'd']
lst2 = ['c', 'a', 'b']
print(isPermutation(lst1, lst2))
