"""
Also called Circular Queue
"""


class Queue:
    def __init__(self, size: int):
        self.items = [None] * size
        self.head = -1
        self.tail = -1

    def __str__(self):
        return " -> ".join([str(v) for v in self.items])

    def isEmpty(self):
        return True if self.head == -1 else False 

    def isFull(self):
        if (self.tail + 1) % len(self.items) == self.head:
            return True 
        else:
            return False 

    def enqueue(self, val):
        if self.isFull():
            raise ValueError("The queue is full")
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % len(self.items)
        self.items[self.tail] = val 

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("The queue is empty")
        val = self.items[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:   
            self.head = (self.head + 1) % len(self.items)

        return val 

q = Queue(4)
print(q)
q.enqueue(1)
print(q)

q.enqueue(2)
print(q)

q.enqueue(3)
print(q)

q.enqueue(4)
print(q)

print(q.dequeue())
print(q)

q.enqueue(5)
print(q)

print(q.dequeue())
print(q)

q.enqueue(6)
print(q)

            


