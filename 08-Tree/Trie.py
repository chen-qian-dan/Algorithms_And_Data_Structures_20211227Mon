# Trie

# create
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfString = False 


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insertString(self, word):
        cur = self.root 
        for ch in word:
            if not ch in cur.children.keys():
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfString = True 
        print("Successfully inserted")


trie = Trie()
trie.insertString("App")
trie.insertString("Appl")

