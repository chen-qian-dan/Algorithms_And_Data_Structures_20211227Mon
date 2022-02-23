"""
Divide and Conquer

395 - Convert string
S1 and S2 are given strings
Convert S2 to S1 using delete, insert or replace operations
Find the minimum count of edit operations
1. problem
2. input: s1, s2
3. output: int
4. edge: ""
5. time: O(N)
6. space:
"""


def convert_str(s1, s2, index1: int, index2: int) -> int:
    if index1 == len(s1):
        return len(s2) - index2 
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return convert_str(s1, s2, index1 + 1, index2 + 1)
    # delete
    sub1 = 1 + convert_str(s1, s2, index1+1, index2)
    # insert
    sub2 = 1 + convert_str(s1, s2, index1, index2 + 1)
    # replace 
    sub3 = 1 + convert_str(s1, s2, index1 + 1, index2 + 1)
    return min(sub1, sub2, sub3)

s1 = ""
s2 = "ttable"
print(convert_str(s1, s2, 0, 0))
