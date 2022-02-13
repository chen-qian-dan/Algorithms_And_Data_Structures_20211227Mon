# Write code to remove duplicates from an unsorted linked list

from Singly_Linked_List import SinglyLinkedList

def removeDuplicates(ll):
    if ll.head is None:
        pass 
    else:
        visited = set()
        visited.add(ll.head.val)
        cur = ll.head
        while cur.next:
            if cur.next.val in visited:
                if cur.next == ll.tail:
                    ll.tail = cur
                    ll.tail.next = None
                else:
                    cur.next = cur.next.next 
            else:
                visited.add(cur.next.val)
                cur = cur.next 

ll = SinglyLinkedList()
ll.add(1)
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(2)
ll.add(1)

print(ll)
removeDuplicates(ll)
print(ll.tail.val)
print(ll)
