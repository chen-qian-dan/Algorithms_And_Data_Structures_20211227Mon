
class Node:
    def __init__(self, val = None):
        self.val = val 
        self.prev = None 
        self.next = None 

class Circular_Doubly_Linked_List:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        cur = self.head 
        while cur:
            yield cur.val 
            if cur.next == self.head:
                break 
            cur = cur.next 

    def __str__(self):
        return str([v for v in self.__iter__()])

    def insert(self, index: int, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode 
            self.tail = newNode 
            self.head.prev = self.tail 
            self.tail.next = self.head 
        elif index == 0:
            newNode.next = self.head 
            self.head.prev = newNode 
            self.head = newNode
            self.tail.next = self.head 
            self.head.prev = self.tail 
        else:
            i = 0
            cur = self.head 
            while i < index - 1 and cur.next != self.head:
                i += 1
                cur = cur.next 
            if cur.next == self.head:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode 
                self.tail.next = self.head 
                self.head.prev = self.tail 
            else:
                newNode.next = cur.next
                cur.next.prev = newNode 
                newNode.prev = cur 
                cur.next = newNode 

    def traverse(self):
        ret = list()
        cur = self.head 
        while cur:
            ret.append(cur.val)
            if cur.next == self.head:
                break 
            cur = cur.next 
        return ret 

    def traverseReversal(self):
        ret = list()
        cur = self.tail
        while cur:
            ret.append(cur.val)
            if cur == self.head:
                break 
            cur = cur.prev 
        return ret 

    def search(self, val):
        if self.head is None:
            print("The list is empty")
        else:
            cur = self.head 
            i = 0
            while cur:
                if cur.val == val:
                    print(i)
                    break 
                if cur == self.tail:
                    print("The node is not in the list")
                    break 
                cur = cur.next 
                i += 1

    def deleteNodeByValue(self, val):
        if self.head is None:
            print("The list is empty")
        elif self.head.val == val:
            if self.head == self.tail:
                self.head.next = None 
                self.head.prev = None 
                self.head = None 
                self.tail = None 
            else:
                node = self.head 
                self.head = self.head.next 
                node.prev = None 
                node.next = None 
                self.head.prev = self.tail 
                self.tail.next = self.head 
            print("Delete it successfully")
        else:
            cur = self.head 
            while cur.next.val != val and cur != self.tail:
                cur = cur.next 
            if cur == self.tail:
                print("The node is not in the list")
            elif cur.next == self.tail:
                node = self.tail 
                self.tail = cur
                node.next = None 
                node.prev = None 
                self.tail.next = self.head 
                self.head.prev = self.tail 
                print("Delete it successfully")
            else:
                node = cur.next 
                cur.next = node.next
                node.next.prev = cur 
                node.next = None 
                node.prev = None 
                print("Delete it successfully")


    def deleteNodeByIndex(self, index: int):
        if self.head is None:
            print("The list is empty")
        elif index == 0:
            if self.head == self.tail:
                node = self.head 
                node.next = None 
                node.prev = None 
                self.head.prev = None 
                self.tail.next = None 
            else:
                node = self.head 
                self.head = self.head.next 
                node.next = None 
                node.prev = None 
                self.head.prev = self.tail 
                self.tail.next = self.head 
            print("Delete it successfully")
        else:
            i = 0
            cur = self.head 
            while i < index - 1 and cur.next != self.head:
                i += 1
                cur = cur.next 
            if cur == self.tail:
                print("index out of range")
            elif cur.next == self.tail:
                node = self.tail 
                self.tail = cur
                node.next = None 
                node.prev = None 
                self.head.prev = self.tail 
                self.tail.next = self.head 
                print("Delete it successfully")
            else:
                node = cur.next 
                cur.next = node.next 
                node.next.prev = cur 
                node.next = None 
                node.prev = None 
                print("Delete it successfully")

    def deleteList(self):
        self.tail.next = None 
        cur = self.head
        while cur:
            cur.prev = None 
            cur = cur.next 
        self.head.prev = None 
        self.head = None 
        self.tail = None 

    
cdll = Circular_Doubly_Linked_List()
cdll.insert(1, 1)
cdll.insert(3, 2)
cdll.insert(3, 3)
print(cdll)
cdll.insert(4, 4)
print(cdll)
# print(cdll.traverse())
# print(cdll.traverseReversal())
# cdll.search(5)
# cdll.deleteNodeByValue(5)
cdll.deleteNodeByIndex(0)
print(cdll)