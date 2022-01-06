# Write code to remove duplicates from an unsorted linked list 

from typing import Set 
from LinkedList import LinkedList, Node 



def removeDuplicates(ll):
    if not ll.head:
        return 
    else:
        curNode: Node = ll.head 
        visitedNode: Set[Node] = set([curNode.value])
        while curNode.next:
            if curNode.next.value in visitedNode:
                if curNode.next == ll.tail:
                    curNode.next = None 
                    ll.tail = curNode
                else:
                    curNode.next = curNode.next.next
            else:
                visitedNode.add(curNode.next.value)
                curNode = curNode.next
        return  


ll = LinkedList()
ll.add(1)
# ll.add(2)
# ll.add(3)
# ll.add(2)
# ll.add(1)

print(ll)
removeDuplicates(ll)
print(ll)

