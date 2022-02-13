"""
Linked List Interview Q
Partition 
Write code to partition a linked list around a value x, 
such that all nodes less than x come before all nodes greater than or equal to x 
"""

"""
1. input: para types 
2. -> output: para types 
3. -> problem define 
4. -> edge cases 
5. -> time complexity
6. -> space complexity

input:
ll: LinkedList
x: int 
output: 
ll?
Q1: are they need to be in order? no
Q2: what kind of linked list? Singly linked list 
Q3: is the list can be empty? yes
Q4: can x smaller / bigger than all items in the list? yes

Q5: can I create a buffer? or have deal with ll in-place? can create buffer 
"""

from Singly_Linked_List import SinglyLinkedList

def partition(ll: SinglyLinkedList, x: int) -> SinglyLinkedList:
    """
    loop through ll, if node value >= x, add and the end, else add at the beginning
    """
    if ll.head is None:
        return None 
    cur = ll.head 
    newLL = SinglyLinkedList()

    while cur:
        if cur.val < x:
            newLL.insert(0, cur.val)
        else:
            newLL.add(cur.val)
        cur = cur.next 

    return newLL


ll: SinglyLinkedList = SinglyLinkedList()
ll.add(1)
ll.add(3)
ll.add(90)
ll.add(40)
ll.add(20)
ll.add(35)
ll.add(12)
ll.add(7)
ll.add(9)
ll.add(45)
print(ll)
print(partition(ll, 1))
# print(ll)

