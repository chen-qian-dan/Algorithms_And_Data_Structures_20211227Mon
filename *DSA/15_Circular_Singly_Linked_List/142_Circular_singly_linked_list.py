

class Node:
    def __init__(self, val = None):
        self.val = val 
        self.next = None 


class Circular_Singly_Linked_List:
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
            self.tail.next = self.head 
        else:
            if index == 0:
                newNode.next = self.head 
                self.head = newNode 
                self.tail.next = self.head 
            else:
                i = 0
                cur = self.head 
                while i < index - 1 and cur.next != self.head:
                    i += 1
                    cur = cur.next 
                if cur.next == self.head:
                    cur.next = newNode 
                    self.tail = newNode
                    self.tail.next = self.head 
                else:
                    newNode.next = cur.next 
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

    def search(self, val):
        cur = self.head
        i = 0
        while cur:
            if cur.val == val:
                return i 
            if cur.next == self.head:
                break 
            cur = cur.next 
            i += 1
        return False 

    def deleteNodeByValue(self, val):
        if self.head is None:
            print("The list is empty")
            return 
    
        if self.head.val == val:
            if self.head == self.tail:
                node = self.head 
                self.head = None
                self.tail = None 
                node.next = None 
            else:
                self.head = self.head.next 
                self.tail.next = self.head 
            print("Delete it successfully")
            return 
        else:
            cur = self.head 
            while cur.next != self.head and cur.next.val != val:
                cur = cur.next 
            if cur.next == self.head:
                print("The node is not in the list")
            elif cur.next == self.tail:
                self.tail.next = None 
                self.tail = cur
                self.tail.next = self.head 
                print("Delete it successfully")
            else:
                cur.next = cur.next.next 
                print("Delete it successfully")

    def deleteNodeByIndex(self, index: int):
        if self.head is None:
            print("The list is empty")
        elif index == 0:
            if self.head == self.tail:
                self.tail.next = None 
                self.head = None 
                self.tail = None 
            else:
                self.head = self.head.next 
                self.tail.next = self.head 
            print("Delete it successfully")
        else:
            i = 0
            cur = self.head 
            while i < index - 1 and cur.next != self.head:
                i += 1
                cur = cur.next 
            if cur == self.tail:
                print("Out of range")
            elif cur.next == self.tail:
                self.tail.next = None 
                self.tail = cur
                self.tail.next = self.head 
                print("Delete it successfully")
            else:
                cur.next = cur.next.next 
                print("Delete it successfully")

    def deleteList(self):
        if self.head is None:
            print("The list is empty")
        else:
            self.tail.next = None 
            self.head = None 
            self.tail = None 




                
csll = Circular_Singly_Linked_List()
csll.insert(1, 1)
csll.insert(3, 2)
csll.insert(2, 3)
# print(csll)
# csll.insert(4, 4)
# print(csll)
# print(csll.traverse())
# print(csll.search(5))

print(csll)
# csll.deleteNodeByValue(3)
csll.deleteNodeByIndex(3)
print(csll)
