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


def removeDuplicatesWithoutBuffer(ll: LinkedList):
    # list is empty
    if not ll.head:
        return 

    # loop node i in range [0, n]
    #   loop node j in range [i + 1, n]
    #       if i.value == j.value:
    #           {remove node j
    #           if j == ll.tail                   
    curNode: Node = ll.head 
    
    while curNode:
        i = curNode
        j = i.next
        while j:
            if curNode.value == j.value:
                # remove j 
                if j == ll.tail:
                    ll.tail = i
                    i.next = None 
                else:
                    i.next = j.next 

                j = i.next
            else:
                i = i.next
                j = i.next 
        curNode = curNode.next

    


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(2)
ll.add(1)

print(ll)
removeDuplicatesWithoutBuffer(ll)
print(ll.tail.value)
print(ll)

