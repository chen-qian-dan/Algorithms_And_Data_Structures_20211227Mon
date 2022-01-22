"""
Divide and Conquer:

399 - Longest Common Sequence Problem
- S1 and S2 are given strings
- Find the length of the longest subsequence which is common to both strings
- Subsequence: a sequence that can be driven from another sequence by deleting some elements without chaning the order of them
Example:
- s1 = "elephant
- s2 = "erepat"
- output = 5
- longest string: "eepat
"""


def findLongestCommonSequence(s1: str, s2: str, index1: int, index2: int) -> int:
    if index1 >= len(s1) or index2 >= len(s2):
        return 0

    if s1[index1] == s2[index2]:
        return 1 + findLongestCommonSequence(s1, s2, index1 + 1, index2 + 1)
    else:
        b = findLongestCommonSequence(s1, s2, index1, index2 + 1)
        c = findLongestCommonSequence(s1, s2, index1 + 1, index2)

        return max(b, c)


s1 = "elephant"
s2 = "erepat"
print(findLongestCommonSequence(s1, s2, 0, 0))


def findLongestCommonSequenceString(s1: str, s2: str, index1: int, index2: int) -> str:
    if index1 >= len(s1) or index2 >= len(s2):
        return ""

    if s1[index1] == s2[index2]:
        return s1[index1] + findLongestCommonSequenceString(s1, s2, index1 + 1, index2 + 1)
    else:
        b = findLongestCommonSequenceString(s1, s2, index1, index2 + 1)
        c = findLongestCommonSequenceString(s1, s2, index1 + 1, index2)

        return b if len(b) > len(c) else c

print(findLongestCommonSequenceString(s1, s2, 0, 0))
