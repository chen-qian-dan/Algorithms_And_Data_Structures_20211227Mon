# check for two given two lists, if they are permutation to each other
# permutation: same items, different / same order


from typing import List

def isPermutation(lstA: List[int], lstB: List[int]) -> bool:
    if len(lstA) != len(lstB):
        return False
    for a in lstA:
        if a not in lstB:
            return False
    return True 