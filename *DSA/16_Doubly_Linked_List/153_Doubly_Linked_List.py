

class Node:
    def __init__(self, val = None):
        self.val = val 
        self.prev = None 
        self.next = None 

class Doubly_Linked_List:
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def __iter__(self):
        cur = self.head 
        while cur:
            yield cur.val 
            if cur is self.tail:
                break 
            cur = cur.next 
    
    def __str__(self):
        return str([v for v in self.__iter__()])

    def insert(self, index: int, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode 
            self.tail = newNode 
        elif index == 0:
            newNode.next = self.head 
            self.head.prev = newNode
            self.head = newNode
        else:
            i = 0
            cur = self.head 
            while i < index - 1 and cur.next:
                i += 1
                cur = cur.next 
            if cur.next is None:
                newNode.prev = self.tail 
                self.tail.next = newNode
                self.tail = newNode 
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
            if cur is self.tail:
                break 
            cur = cur.next 

    def reverse(self):
        if self.head is None:
            print("The list is empty")
        elif self.head == self.tail:
            # do nothing
            pass 
        else:
            l = None
            r = self.head
            while r:
                r.prev = r.next 
                r.next = l 
                l = r
                r = r.prev

            self.head, self.tail = self.tail, self.head

    def search(self, val):
        if self.head is None:
            print("The list is empty")
        else:
            i = 0
            cur = self.head 
            while cur:
                if cur.val == val:
                    print(i)
                    return 
                else:
                    i += 1
                    cur = cur.next 
            print("The node is not in the list")

    def deleteNodeByValue(self, val):
        if self.head is None:
            print("The list is empty")
            return 
        if self.head.val == val:
            if self.head == self.tail:
                self.head = None 
                self.tail = None 
            else:
                self.head = self.head.next 
                self.head.prev = None 
            print("delete at 0")
        else:
            i = 0 
            cur = self.head 
            while cur.next and cur.next.val != val:
                cur = cur.next 
                i += 1
            if cur.next is None:
                print("The value is not in the list")
            elif cur.next == self.tail:
                cur.next = None 
                self.tail = cur 
                print(f"Delete at {i+1}")
            else:
                node = cur.next 
                cur.next = node.next 
                node.next.prev = cur 
                node.next = None 
                node.prev = None 
                print(f"Delete at {i+1}")


    def deleteNodeByIndex(self, index: int):
        if self.head is None:
            print("The list is empty")
        elif index == 0:
            if self.head == self.tail:
                self.head = None 
                self.tail = None 
            else:
                self.head = self.head.next 
                self.head.prev = None 
            print(f"Delete at {index}")
        else:
            i = 0
            cur = self.head 
            while i < index - 1 and cur.next:
                i += 1
                cur = cur.next 
            if cur.next is None:
                print("Index out of range")
            elif cur.next == self.tail:
                cur.next = None
                self.tail = cur 
                print(f"Delete at {index}")
            else:
                cur.next = cur.next.next
                cur.next.prev = cur 
                print(f"Delete at {index}")


    def deleteList(self):
        cur = self.head 
        while cur:
            cur.prev = None 
            cur = cur.next 
        self.head = None
        self.tail = None 

                






    
dll = Doubly_Linked_List()
dll.insert(1, 1)
dll.insert(1, 2)
dll.insert(2, 3)
print(dll)
dll.insert(4, 4)
print(dll)
# dll.reverse()
# print(dll)
# dll.search(5)
# dll.deleteNodeByValue(5)
dll.deleteNodeByIndex(4)
print(dll)