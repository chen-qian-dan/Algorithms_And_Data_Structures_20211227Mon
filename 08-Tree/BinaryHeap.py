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


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = index // 2
    if index <= 1:
        return 
    if heapType == "Min":
        if rootNode.list[index] < rootNode.list[parentIndex]:
            temp = rootNode.list[parentIndex]
            rootNode.list[parentIndex] = rootNode.list[index]
            rootNode.list[index] = temp 
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.list[index] > rootNode.list[parentIndex]:
            temp = rootNode.list[parentIndex]
            rootNode.list[parentIndex] = rootNode.list[index]
            rootNode.list[index] = temp 
        heapifyTreeInsert(rootNode, parentIndex, heapType)
        

def insertNode(rootNode, value, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The binary Heap is full"

    rootNode.heapSize += 1
    rootNode.list[rootNode.heapSize] = value 
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value is inserted successfully"
    




heap = Heap(5)
print(peekofHeap(heap))
print(sizeofHeap(heap))
insertNode(heap, 4, "Max")
insertNode(heap, 5, "Max")
insertNode(heap, 2, "Max")
insertNode(heap, 1, "Max")
levelTraverse(heap)