# queue_usingPythonList_noSizeLimit

class Queue:
    def __init__(self):
        self.items = list()

    def __str__(self):
        values = [str(v) for v in self.items]
        return ' '.join(values)

    def isEmpty(self):
        return True if len(self.items) == 0 else False 

    def enqueue(self, value): # O(1)
        self.items.append(value)
        return "Enqueue successfully"

    def dequeue(self): # O(n)
        if self.isEmpty():
            return "The queue is empty"
        value = self.items.pop(0)
        return value 

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        return self.items[0]



q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)
print(q.dequeue())
print(q)
print(q.peek())
    