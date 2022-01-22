"""
Divide and Conquer

395 - Convert string
S1 and S2 are given strings
Convert S2 to S1 using delete, insert or replace operations
Find the minimum count of edit operations

1. problem s2 -> s1
delete
insert
replace 
2. intput: s1, s2
3. output: count: int 
4. edge case
s1 = [], or s2 = []
5. time complexity
6. space complexity
"""


def minConvertString(s1: str, s2: str, index1: int, index2: int) -> int:
    """
    for the 1st char in s2, there are 3 cases:
    1. delete it
    2. insert(0, s1[0])
    3. replace with s1[0]
    """
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    if index1 >= len(s1):
        return len(s2) - index2
    if index2 >= len(s2):
        return len(s1) - index1

    if s1[index1] == s2[index2]:
        return minConvertString(s1, s2, index1 + 1, index2 + 1)
        
    else:
        d = 1 + minConvertString(s1, s2, index1, index2 + 1)
        i = 1 + minConvertString(s1, s2, index1 + 1, index2)
        r = 1 + minConvertString(s1, s2, index1 + 1, index2 + 1)
    
    return min(d, i, r)

s1 = "table"
s2 = "tbres" # expect 3

print(minConvertString(s1, s2, 0, 0))

