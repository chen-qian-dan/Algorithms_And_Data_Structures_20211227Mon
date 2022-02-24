"""
Divide and Conquer:

399 - Longest Common Sequence Problem
- S1 and S2 are given strings
- Find the length of the longest subsequence which is common to both strings
- Subsequence: a sequence that can be driven from another sequence by deleting some elements without chaning the order of them
Example:
- s1 = "lephant
- s2 = "erepat"
- output = 5
- longest string: "eepat

abcde, subsequence of 3 are: abc, ace, ade, cde, etc
1. problem
2. input: s1, s2, 
3. output: int
4. edeg: ""
5. time
6. space
"""

def get_longest_common_subsequence(s1, s2, index1, index2) -> int:
    if index1 >= len(s1) or index2 >= len(s2):
        return 0 
    if s1[index1] == s2[index2]:
        return 1 + get_longest_common_subsequence(s1, s2, index1 + 1, index2 + 1)
    else:
        sub1 = get_longest_common_subsequence(s1, s2, index1 + 1, index2)
        sub2 = get_longest_common_subsequence(s1, s2, index1, index2 + 1)
        return max(sub1, sub2)


def get_longest_common_subsequence_str(s1, s2, index1, index2) -> int:
    if index1 >= len(s1) or index2 >= len(s2):
        return "" 
    if s1[index1] == s2[index2]:
        return s1[index1] + get_longest_common_subsequence_str(s1, s2, index1 + 1, index2 + 1)
    else:
        sub1 = get_longest_common_subsequence_str(s1, s2, index1 + 1, index2)
        sub2 = get_longest_common_subsequence_str(s1, s2, index1, index2 + 1)
        return sub1 if len(sub1) > len(sub2) else sub2



s1 = "elephant"
s2 = "erepat"
print(get_longest_common_subsequence(s1, s2, 0, 0))

print(get_longest_common_subsequence_str(s1, s2, 0, 0))



