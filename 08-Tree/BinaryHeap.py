# Binary Heap:


# create
class Heap:
    def __init__(self, maxSize: int):
        self.list = [None] * (maxSize + 1)
        self.maxSize: int = maxSize + 1
        self.size: int = 0 

def peekofHeap(rootNode):
    if not rootNode:
        return 
    return rootNode.list[1]


heap = Heap(5)
print(peekofHeap(heap))