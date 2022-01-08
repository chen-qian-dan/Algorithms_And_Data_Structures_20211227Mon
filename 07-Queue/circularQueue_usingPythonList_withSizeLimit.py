# circularQueue_usingPythonList_withSizeLimit

class Queue:
    def __init__(self, maxSize):
        self.items = [None] * maxSize
        self.maxSize = maxSize 
        self.outIndex = -1
        self.inIndex = -1