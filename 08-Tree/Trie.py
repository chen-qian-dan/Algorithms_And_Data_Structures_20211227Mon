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


def deleteString(root, word, index):
    # check if the word in this trie
    # if yes, then start from the leaf node 
    # case 1: some other prefix of string is same as the one that we want to delete (API, APPLE)
    # case 2: word is a prefix of another string (API, APIS)
    # case 3: other string is a prefix of word(APIS, AP)
    # case 4: not any node depends on word
    if not root.searchString(word):
        print ("The word does not in trie")
        return 

    ch = word[index]
    cur = root.children.get(ch)
    canThisNodeBeDeleted = False 

    if len(cur.children) > 1:
        deleteString(cur, word, index + 1)
        return False 

    if index == len(word) - 1:
        if len(cur.children) >= 1:
            cur.endOfString = False 
            return False 
        else:
            root.children.pop(ch)
            return True 
    if cur.endOfString:
        deleteString(cur, word, index + 1)
        return False 

    canThisNodeBeDeleted = deleteString(cur, word, index + 1)
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        return True 
    else:
        return False 

    

    


trie = Trie()
trie.insertString("App")
trie.insertString("Appl")
# print(trie.searchString("Ap"))
# print(trie.searchStringVideo("Ap"))
deleteString(trie.root, "App", 0)
print(trie.searchString("APP"))

