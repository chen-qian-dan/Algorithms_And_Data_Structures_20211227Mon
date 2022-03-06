class Heap:
    def __init__(self, size: int):
        self.lst = [None] * (size + 1)
        self.heapSize = 0 
        self.maxSize = size + 1



# peak : return List[1] time O(1), space O(1)
def peak(root):
    if not root:
        return None 
    else:
        return root.lst[1]


# size of binary heap
# return number of filled cells time O(1), space O(1)
def sizeOfHeap(root):
    if not root:
        return None 
    else:
        return root.heapSize


# traversal time O(n), space O(n)
# pre-order, in-order, post-order, level order 
def levelOrderTraversal(root):
    if not root:
        return None 
    else:
        ret = list()
        for i in range(1, root.heapSize + 1):
            ret.append(root.lst[i])
        return ret 

# insert a node to binary heap 
# insert at the end of the list
# loop the list from the end to the begining, swap value if it is not smaller than its parent
def heapify(root, index: int, heapType): # time O(logN), space O(logN)
    parentIndex = index // 2
    if index <= 1:
        return None 
    if heapType == "Min":
        if root.lst[index] < root.lst[parentIndex]:
            root.lst[index], root.lst[parentIndex] = root.lst[parentIndex], root.lst[index]
            heapify(root, parentIndex, heapType)
    if heapType == "Max":
        if root.lst[index] > root.lst[parentIndex]:
            root.lst[index], root.lst[parentIndex] = root.lst[parentIndex], root.lst[index]
            heapify(root, parentIndex, heapType)

def insertNode(root, value, heapType): # time O(logN), space O(logN)
    if root.heapSize + 1 == root.maxSize:
        return "The binary heap is full"
    root.lst[root.heapSize + 1] = value 
    root.heapSize += 1
    heapify(root, root.heapSize, heapType)
    return "The value has been successfully inserted"


# Creation : time O(1), space O(N)
heap = Heap(5)
print(sizeOfHeap(heap))
print(peak(heap))
print(levelOrderTraversal(heap))
insertNode(heap, 2, "Max")
insertNode(heap, 5, "Max")
insertNode(heap, 4, "Max")
insertNode(heap, 1, "Max")
print(levelOrderTraversal(heap))




