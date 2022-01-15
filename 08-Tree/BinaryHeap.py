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


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = leftIndex + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return 
    elif rootNode.heapSize == leftIndex: # only have leftIndex 
        if heapType == "Min":
            if rootNode.list[index] > rootNode.list[leftIndex]:
                temp = rootNode.list[index]
                rootNode.list[index] = rootNode.list[leftIndex]
                rootNode.list[leftIndex] = temp 
            return 
        else:
            if rootNode.list[index] < rootNode.list[leftIndex]:
                temp = rootNode.list[index]
                rootNode.list[index] = rootNode.list[leftIndex]
                rootNode.list[leftIndex] = temp 
            return 
    else:
        if heapType == "Min":
            if rootNode.list[index] > min(rootNode.list[index * 2], rootNode.list[index * 2 + 1]):
                if rootNode.list[index * 2] < rootNode.list[index * 2 + 1]:
                    temp = rootNode.list[index]
                    rootNode.list[index] = rootNode.list[index * 2]
                    rootNode.list[index * 2] = temp 
                    index = index * 2
                else:
                    temp = rootNode.list[index]
                    rootNode.list[index] = rootNode.list[index * 2 + 1]
                    rootNode.list[index * 2 + 1] = temp 
                    index = index * 2 + 1
                heapifyTreeExtract(rootNode, index, heapType)
            else:
                return 
            
        else:
            if rootNode.list[index] < max(rootNode.list[index * 2], rootNode.list[index * 2 + 1]):
                if rootNode.list[index * 2] > rootNode.list[index * 2 + 1]:
                    temp = rootNode.list[index]
                    rootNode.list[index] = rootNode.list[index * 2]
                    rootNode.list[index * 2] = temp 
                    index = index * 2
                else:
                    temp = rootNode.list[index]
                    rootNode.list[index] = rootNode.list[index * 2 + 1]
                    rootNode.list[index * 2 + 1] = temp 
                    index = index * 2 + 1

                heapifyTreeExtract(rootNode, index, heapType)
            else:
                return 


def extractNode(rootNode, heapType):

    if rootNode.heapSize == 0:
        return 

    extractedNode = rootNode.list[1]
    rootNode.list[1] = rootNode.list[rootNode.heapSize]
    rootNode.list[rootNode.heapSize] = None 
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractedNode


def deleteEntireBP(rootNode):
    rootNode.list = None 
    




heap = Heap(5)
insertNode(heap, 4, "Max")
insertNode(heap, 5, "Max")
insertNode(heap, 2, "Max")
insertNode(heap, 1, "Max")
levelTraverse(heap)
print("Extract -------------")
print(extractNode(heap, "Max"))
print("Extract -------------")
levelTraverse(heap)
