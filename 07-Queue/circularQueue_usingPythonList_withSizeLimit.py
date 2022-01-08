# circularQueue_usingPythonList_withSizeLimit

class CircularQueue:
    def __init__(self, maxSize):
        self.items = [None] * maxSize
        self.maxSize = maxSize 
        self.headIndex = -1
        self.tailIndex = -1

    def __str__(self):
        values = [str(v) for v in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.headIndex == 0 and self.tailIndex == self.maxSize - 1:
            return True 
        elif self.tailIndex + 1 == self.headIndex:
            return True 
        else:
            return False 


    def isEmpty(self):
        return True if self.headIndex == -1 else False 



cq = CircularQueue(6)
print(cq.isFull())
print(cq.isEmpty())