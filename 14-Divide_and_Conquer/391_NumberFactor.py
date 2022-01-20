"""
Divid and Conquer:
Number Factor
Given N, find the number of ways to express N as a sum of 1, 3, and 4
example:
N = 4, 
number of ways = 4
they are: {4}, {1, 3}, {3, 1}, {1, 1, 1, 1}
"""
from typing import List 

def numberFactor(n: int, numbers: List[int]):
    if n < 0:
        return 
    if n == 0:
        return [[]]
    
    ret = list()
    for v in numbers:
        sub = numberFactor(n - v, numbers)
        if sub:
            for s in sub:
                s.append(v)
                ret.append(s)

    return ret 


numbers = [1, 3, 4]
print(numberFactor(4, numbers))

