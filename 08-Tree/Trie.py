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


    def searchString(self, word):
        cur = self.root
        for ch in word:
            if not ch in cur.children.keys():
                return False 
            if len(cur.children.keys()) == 0:
                return False 
            cur = cur.children[ch]
        if cur.endOfString:
            return True 
        else:
            return False 


    def searchStringVideo(self, word):
        cur = self.root
        for ch in word:
            node = cur.children.get(ch)
            if not node:
                return False 
            cur = node 

        if cur.endOfString is True:
            return True 
        else:
            return False 


    


trie = Trie()
trie.insertString("App")
trie.insertString("Appl")
print(trie.searchString("Ap"))
print(trie.searchStringVideo("Ap"))

