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

    def enqueue(self, value):
        if self.isFull():
            print("The queue is full")
            return 
        if self.headIndex == -1:
            self.headIndex = 0
            self.tailIndex = 0
            self.items[self.tailIndex] = value 
        else:
            self.tailIndex += 1
            
            if self.tailIndex == self.maxSize:
                self.tailIndex = 0
                
            self.items[self.tailIndex] = value 

    def dequeue(self):
        if self.headIndex == -1:
            return "The queue is empty"
        else:
            value = self.items[self.headIndex]
            if self.headIndex == self.tailIndex:
                self.headIndex = -1
                self.tailIndex = -1
            else:
                self.items[self.headIndex] = None 
                self.headIndex += 1
                if self.headIndex == self.maxSize:
                    self.headIndex = 0
            return value 

    def peek(self):
        if self.headIndex == -1:
            return "The queue is empty"
        else:
            return self.items[self.headIndex]




cq = CircularQueue(6)
print(cq.isFull())
print(cq.isEmpty())
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq)
print(cq.dequeue())
print(cq)
print(cq.peek())