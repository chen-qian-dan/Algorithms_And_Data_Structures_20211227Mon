# Trie

# create
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfString = False 


class Trie:
    def __init__(self):
        self.root = TrieNode()

trie = Trie()
