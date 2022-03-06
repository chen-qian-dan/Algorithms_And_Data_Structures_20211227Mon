class Heap:
    def __init__(self, size: int):
        self.lst = [None] * (size + 1)
        self.heapSize = 0 
        self.maxSize = size + 1

def peak(root):
    if not root:
        return None 
    else:
        return root.lst[1]



# Creation : time O(1), space O(N)
heap = Heap(5)

# peak : return List[1] time O(1), space O(1)

