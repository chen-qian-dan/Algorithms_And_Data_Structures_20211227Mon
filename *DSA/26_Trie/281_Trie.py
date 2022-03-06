"""
1. Creation
2. Insertion in Trie
3. Search for a string in Trie 
4. Deletion from Trie 
"""

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfString = False 

class Trie:
    def __init__(self):
        self.root = TrieNode() 


trie = Trie() # create Trie : time O(1), space O(1)
