"""
Write a function to find all pairs of an integer array whose sum is equal to a given number

pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
output: ['2+5', '4+3', '3+4', '-2+9']
"""

from typing import List
def pairSum(lst: List[int], targetNumber: int) -> List[str]:
    ret = list()
    visited = dict() 
    for i, v in enumerate(lst):
        if v in visited.keys():
            j = visited[v]
            pair = f"{lst[j]}+{lst[i]}"
            ret.append(pair)
        
        visited[targetNumber - v] = i 
    return ret 


ret = pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
print(ret)