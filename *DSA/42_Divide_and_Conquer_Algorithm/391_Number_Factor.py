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

def get_number_factor(N: int, factors):
    if N in (0, 1, 2):
        return 1
    elif N == 3:
        return 2
    else:
        subP1 = get_number_factor(N - 1, factors)
        subP2 = get_number_factor(N - 3, factors)
        subP3 = get_number_factor(N - 4, factors)
        return subP1 + subP2 + subP3



def get_number_factor_list(N: int, factors): # O(len(factors)^(N-1))
    if N < 0:
        return []
    elif N == 0:
        return [[]]
    else:
        ret = list()
        for f in factors:
            sub = get_number_factor_list(N - f, factors)
        
            for v in sub:
                v.append(f)
                ret.append(v)

        return ret 

N = 4
factors = [1, 3, 4]
print(get_number_factor(N, factors))

print(get_number_factor_list(N, factors))