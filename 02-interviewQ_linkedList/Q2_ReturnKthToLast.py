"""
Return Nth to Last
Implement an algorithm to find the nth to last element of a singly linked list. 
head -> node1 -> node2 -> node3 -> node4 
2th to lask is node3
"""
from LinkedList import LinkedList, Node 

def nthToLast(ll: LinkedList, n: int):
    i: Node = ll.head 
    j: Node = ll.head 
    for k in range(n - 1):
        j = j.next 
    
    while j != ll.tail:
        i = i.next 
        j = j.next 
    return i 


ll: LinkedList = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
print(nthToLast(ll, 3).value)

