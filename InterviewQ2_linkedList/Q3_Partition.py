"""
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
from LinkedList import LinkedList, Node 

def partition(ll: LinkedList, x: int) -> LinkedList:
    # list is empty / only one node, do nothing, return newll
    # loop through ll, if node < x, insert before x, otherwise, insert after x
    # remove node x 

    if not ll.head or ll.head == ll.tail:
        return ll 

    newll: LinkedList = LinkedList()
    newll.add(x)
    nodeX: Node = newll.head
    prevX: Node = newll.head
    nextX: Node = newll.head

    curNode: Node = ll.head
    while curNode: 
        node = Node(curNode.value)
        if node.value < x:
            # insert before nodeX
            if newll.head == newll.tail:
                node.next = nodeX 
                newll.head = node 
            else:
                node.next = nodeX 
                prevX.next = node
            prevX = node  
        else:
            # insert after nodeX
            if newll.head == newll.tail:
                nodeX.next = node 
                newll.tail = node 
            else:
                if nodeX == newll.tail:
                    nodeX.next = node 
                    newll.tail = node 
                else:
                    node.next = nextX
                    nodeX.next = node 
            nextX = node 
        curNode = curNode.next
    
    # remove X
    if newll.head == nodeX:
        newll.head = nodeX.next
    elif newll.tail == nodeX:
        prevX.next = None 
        newll.tail = prevX
    else:
        prevX.next = nextX
             
    return newll



def partitionVideo(ll, x):
    curNode = ll.head 
    ll.tail = ll.head 

    while curNode:
        nextNode = curNode.next 
        curNode.next = None 
        if curNode.value < x:
            curNode.next = ll.head 
            ll.head = curNode 
        else:
            ll.tail.next = curNode
            ll.tail = curNode 
        curNode = nextNode 

    # if ll.tail.next is not None:
    #     ll.tail.next = None 





ll: LinkedList = LinkedList()
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
partitionVideo(ll, 40)
print(ll)
