
"""
Karat_20220123Sun 
1. problem: either 0 / 1 match
2. input: List[str], str
3. output: None / a word 
4. edge case: 
    not empty list
    not empty str
5. time complexity  # time O(W*S)
6. space complecity O(W*S)
"""



words = ["cat", "baby", "dog", "bird", "car", "ax"]
string1 = "tcabnihjs"
string2 = "tbcanihjs"
string3 = "baykkjl"
string4 = "bbabylkkj"
string5 = "ccc"
string6 = "breadmaking"


# wordsCount = [{'c': 1, "a":1, "t":1}"cat", "baby", "dog", "bird", "car", "ax"]


from typing import List, Optional, Dict 

def isMatch(word: Dict[str, int], string: str) -> bool: # "tcabnihjs".count(c) = 0 O(S)
    for char in word.keys():
        if word[char] > string.count(char):
            return False
    return True
    
def find_embedded_word(words: List[str], string: str) -> Optional[str]:
    # convert words to List of dict
    wordsCount = list()    # O(W * S)
    for s in words:
        temp = dict()
        for char in s:
            if char not in temp.keys():
                temp[char] = 1
            else:
                temp[char] += 1
        wordsCount.append(temp)
        
    for k, word in enumerate(wordsCount): # time O(W*S)
        if isMatch(word, string):
            return words[k]
        
    return None 

# print(find_embedded_word(words, string1)) # cat
# print(find_embedded_word(words, string2)) # cat
# print(find_embedded_word(words, string3)) # None 
# print(find_embedded_word(words, string4)) # baby
# print(find_embedded_word(words, string5)) # None 
# print(find_embedded_word(words, string6)) # bird
        
        
# After catching your classroom students cheating before, you realize your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

# Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

# grid1 = [
# 	['c', 'c', 'x', 't', 'i', 'b'],
# 	['c', 'c', 'a', 't', 'n', 'i'],
# 	['a', 'c', 'n', 'n', 't', 't'],
# 	['t', 'c', 's', 'i', 'p', 't'],
# 	['a', 'o', 'o', 'o', 'a', 'a'],
# 	['o', 'a', 'a', 'a', 'o', 'o'],
# 	['k', 'a', 'i', 'c', 'k', 'i'],
# ]
# word1 = "catnip"
# word2 = "cccc"
# word3 = "s"
# word4 = "bit"
# word5 = "aoi"
# word6 = "ki"
# word7 = "aaa"
# word8 = "ooo"

# grid2 = [['a']]
# word9 = "a"

# find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
# find_word_location(grid1, word2) =>
#        [(0, 1), (1, 1), (2, 1), (3, 1)]
#     OR [(0, 0), (1, 0), (1, 1), (2, 1)]
#     OR [(0, 0), (0, 1), (1, 1), (2, 1)]
#     OR [(1, 0), (1, 1), (2, 1), (3, 1)]
# find_word_location(grid1, word3) => [(3, 2)]
# find_word_location(grid1, word4) => [(0, 5), (1, 5), (2, 5)]
# find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
# find_word_location(grid1, word6) => [(6, 4), (6, 5)]
# find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
# find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
# find_word_location(grid2, word9) => [(0, 0)]

# Complexity analysis variables:

# r = number of rows
# c = number of columns
# w = length of the word



grid1 = [
	['c', 'c', 'x', 't', 'i', 'b'],
	['c', 'c', 'a', 't', 'n', 'i'],
	['a', 'c', 'n', 'n', 't', 't'],
	['t', 'c', 's', 'i', 'p', 't'],
	['a', 'o', 'o', 'o', 'a', 'a'],
	['o', 'a', 'a', 'a', 'o', 'o'],
	['k', 'a', 'i', 'c', 'k', 'i']
]

word1 = "catnip"
word2 = "cccc"
word3 = "s" 
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

"""
1. problem
2. input
3. output: list
4. edge case: always 1+ solution
5. time complexity
6. space complexity
"""

def find_word_location(grid, word):
    """
    divide and conquer
    """
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            ret = contain(grid1, r, c, word, 0)
            if ret is not None:
                print(ret)
                return 


def contain(grid, r: int, c: int, word: str, index: int):
    if index >= len(word):
        return []

    if r >= len(grid) or c >= len(grid[0]):
        return None

    if grid[r][c] == word[index]:
        right = contain(grid, r, c+1, word, index+1)
        if right is not None:
            return [(r, c)] + right
        down = contain(grid, r+1, c, word, index+1)
        if down is not None:
            return [(r, c)] + down 
           
    return None  


        
word1 = "catnip"
word2 = "cccc"
word3 = "s" 
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"


find_word_location(grid1, word1)
# find_word_location(grid1, word2)
# find_word_location(grid1, word4)
# find_word_location(grid1, word5)
# find_word_location(grid1, word6)
# find_word_location(grid1, word7)
# find_word_location(grid1, word8)

# find_word_location(grid2, word9)
        
    
    

