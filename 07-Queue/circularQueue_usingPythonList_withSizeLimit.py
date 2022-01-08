# circularQueue_usingPythonList_withSizeLimit

class CircularQueue:
    def __init__(self, maxSize):
        self.items = [None] * maxSize
        self.maxSize = maxSize 
        self.outIndex = -1
        self.inIndex = -1

    def __str__(self):
        values = [str(v) for v in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.inIndex == 0 and self.outIndex == self.maxSize - 1:
            return True 
        elif self.outIndex + 1 == self.inIndex:
            return True 
        else:
            return False 



cq = CircularQueue(6)
print(cq.isFull())