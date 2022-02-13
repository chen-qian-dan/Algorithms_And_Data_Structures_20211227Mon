"""
Linked List Interview Q
Find the nth to last element of a singly linked list
"""

from Singly_Linked_List import SinglyLinkedList

def nthToLast(ll: SinglyLinkedList, n: int):
    if ll.head is None:
        raise ValueError("The list is empty")
    else:
        i = 0
        cur = ll.head 
        while i < n and cur:
            i += 1
            cur = cur.next 
        if cur is None:
            return "Index out of range"
        else:
            ret = list()
            while cur:
                ret.append(cur.val)
                cur = cur.next 
            return ret 


ll = SinglyLinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)

print(ll)
print(nthToLast(ll, 6))