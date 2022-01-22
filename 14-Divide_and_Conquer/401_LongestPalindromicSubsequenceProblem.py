
"""
Divide and Conquer:
401 - Longest Palindromic Subsequence Problem
- Given a string S
- Find the longest palindromic subsequence (LPS)
- Subsequence: a sequence that can be driven from another sequence by deleting some elements without changing the order of them
- Palindrome is a string that reads the same backward as well as forward

Example:
- S = "ELRMENMET"
- output = 5
- LPS = "EMEME"

Example:
- S = "AMEEWMEA"
- output = 6
- LPS = "AMEEMA"

1. problem
2. input: str
3. output: str
4. edge case:
 s = ""
5. time complexity
6 space complexity
"""


def findLongestCommonSubString(s1: str, s2: str, index1: int, index2: int) -> str:
    if index1 >= len(s1):
        return ""
    if index2 >= len(s2):
        return ""

    if s1[index1] == s2[index2]:
        return s1[index1] + findLongestCommonSubString(s1, s2, index1 + 1, index2 + 1)
    else:
        a = findLongestCommonSubString(s1, s2, index1, index2 + 1)
        b = findLongestCommonSubString(s1, s2, index1 + 1, index2)
        return a if len(a) > len(b) else b


def findLPS(s: str) -> str:
    s1 = s
    s2 = s[::-1]
    return findLongestCommonSubString(s1, s2, 0, 0)


s = "AMEEWMEA"
print(findLPS(s))


def findLPSVideo(s: str, startIndex: int, endIndex: int) -> str:
    if startIndex > endIndex:
        return ""
    if startIndex == endIndex:
        return s[startIndex]
    
    if s[startIndex] == s[endIndex]:
        return s[startIndex] + findLPSVideo(s, startIndex + 1, endIndex - 1) + s[endIndex]
    else:
        a = findLPSVideo(s, startIndex, endIndex - 1) 
        b = findLPSVideo(s, startIndex + 1, endIndex) 

        return a if len(a) >= len(b) else b


print(findLPSVideo(s, 0, len(s) - 1))
