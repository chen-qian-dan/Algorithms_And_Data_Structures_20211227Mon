from re import I


class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        node = self.head 
        while node:
            yield node.val 
            node = node.next 

    def __str__(self):
        return str([n for n in self.__iter__()])


    def insert(self, index: int, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode 
            self.tail = newNode 
        else:
            if index == 0:
                newNode.next = self.head 
                self.head = newNode 
            else:
                cur = self.head 
                i = 0
                while i < index - 1 and cur:
                    cur = cur.next
                    i += 1
                if cur is None or cur.next is None:
                    self.tail.next = newNode
                    self.tail = self.tail.next 
                else:
                    newNode.next = cur.next 
                    cur.next = newNode


    def traverse(self):
        if self.head is None:
            print()
        ret = list()
        cur = self.head 
        while cur:
            ret.append(cur.val)
            cur = cur.next 
        print(ret)


    def search(self, val):
        if self.head is None:
            return -1
        cur = self.head 
        i = 0
        while cur:
            if cur.val == val:
                return i 
            cur = cur.next 
            i += 1
        return -1 

    def deleteByValue(self, val):
        if self.head is None:
            raise ValueError("Can not delete a value on an empty list")
        
        if self.head.val == val:
            if self.head == self.tail:
                self.head = None 
                self.tail = None 
            else:
                self.head = self.head.next 
        else:
            cur = self.head 
            while cur.next and cur.next.val != val:
                cur = cur.next 
            if cur.next is None:
                print("The value is not in the list")
            elif cur.next == self.tail:
                cur.next = None 
                self.tail = cur 
            else:
                cur.next = cur.next.next 


    def deleteByIndex(self, index: int):
        if self.head is None:
            raise ValueError("The list is empty")
        if index == 0:
            if self.head == self.tail:
                self.head = None 
                self.tail = None 
            else:
                self.head = self.head.next 
        else:
            i = 0
            cur = self.head 
            while i < index - 1 and cur.next:
                cur = cur.next 
                i += 1
            if cur.next is None:
                raise ValueError("index is out of range")
            else:
                cur.next = cur.next.next 
                if cur.next is None:
                    self.tail = cur 

    def deleteList(self):
        self.head = None 
        self.tail = None 


    def add(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode 


    

# sll = SinglyLinkedList()
# sll.insert(0, 1)
# sll.insert(3, 2)
# # sll.insert(3, 3)
# # print(sll)
# # sll.insert(5, 4)
# # print(sll)
# # sll.traverse()
# # print(sll.search(1))

# print(sll)
# sll.deleteByValue(1)
# # sll.deleteByIndex(5)
# print(sll)
