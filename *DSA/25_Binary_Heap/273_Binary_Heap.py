class Heap:
    def __init__(self, size: int):
        self.lst = [None] * (size + 1)
        self.heapSize = 0 
        self.maxSize = size + 1


# Creation : time O(1), space O(N)
heap = Heap(5)
