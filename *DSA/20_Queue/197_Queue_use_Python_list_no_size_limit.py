class Queue:
    def __init__(self) -> None:
        self.q = list()

    def __str__(self):
        return ' -> '.join(str(v) for v in self.q)

    def isEmpty(self):
        return True if len(self.q) == 0 else False 

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("The queue is empty")
        return self.q.pop(0)

    def peek(self):
        if self.isEmpty():
            raise ValueError("The queue is empty")
        return self.q[0]

    def deleteQueue(self):
        self.q.clear()


    
q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)
print(q.dequeue())
print(q)
print(q.peek())
q.deleteQueue()