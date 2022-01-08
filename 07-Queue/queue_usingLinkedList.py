# queue_usingLinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next 

    def __str__(self):
        values = [str(node.value) for node in self]
        return ' '.join(values)

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            self.tail.next = node 
            self.tail = node 

    def isEmpty(self):
        return True if not self.head else False 

    def dequeue(self):
        if not self.head:
            return "The queue is empty"
        else:
            value = self.head 
            self.head = self.head.next 
            return value 

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.isEmpty())
print(q.dequeue())
print(q.dequeue())


    

