# Binary Heap:


# create
class Heap:
    def __init__(self, maxSize: int):
        self.list = [None] * (maxSize + 1)
        self.maxSize: int = maxSize + 1
        self.heapSize: int = 0 

def peekofHeap(rootNode):
    if not rootNode:
        return 
    return rootNode.list[1]


def sizeofHeap(rootNode):
    if not rootNode:
        return 
    return rootNode.heapSize


def levelTraverse(rootNode):
    if not rootNode:
        return 
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.list[i])


heap = Heap(5)
print(peekofHeap(heap))
print(sizeofHeap(heap))