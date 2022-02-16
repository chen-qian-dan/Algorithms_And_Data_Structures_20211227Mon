class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

class Linked_List:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __str__(self):
        ret = list()
        cur = self.head 
        while cur:
            ret.append(str(cur.val))
            cur = cur.next 
        return " -> ".join(ret)

    def isEmpty(self):
        return True if self.head is None else False 

    def push(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = self.tail.next 

    def pop(self):
        if self.head is None:
            raise ValueError("The list is empty")
        if self.head == self.tail:
            val = self.head.val 
            self.head = None 
            self.tail = None 
            return val 
        else:
            val = self.head.val 
            self.head = self.head.next
            return val 


class Queue:
    def __init__(self) -> None:
        self.linkedList = Linked_List()

    def __str__(self):
        return str(self.linkedList)

    def enqueue(self, val):
        self.linkedList.push(val)

    def dequeue(self):
        return self.linkedList.pop()

    def peek(self):
        if self.linkedList.isEmpty():
            raise ValueError("The queue is empty")
        else:
            return self.linkedList.head.val 



q = Queue()
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

