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

    def insertString(self, word): # time O(m), space O(m) m is the len of word
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfString = True 

    def search(self, word): # time O(m) space O(1) m is the len of word 
        cur = self.root 
        for c in word:
            if not c in cur.children:
                return False 
            cur = cur.children[c]
        if cur.endOfString:
            return True 
        return False 


trie = Trie() # create Trie : time O(1), space O(1)


# insert a string in a Trie 
"""
1. The trie is blank 
2. new string's prefix is common to another strings prefix 
"""
trie.insertString("App")
trie.insertString("Appi")


# search a string in trie 

print(trie.search("Appi"))