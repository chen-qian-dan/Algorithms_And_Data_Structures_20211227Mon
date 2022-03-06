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

# Creation : time O(1), space O(N)
heap = Heap(5)
print(sizeOfHeap(heap))
print(peak(heap))


