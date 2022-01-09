"""
Q5: Intersection 
Given two (singly) linked lists, determine if the two lists intersect. 
Return the intersecting node. 
Note that the intersection is defined based on reference, not value. 
That is, if the kth node of the first linked list is the exact same node (by ref) as the jth node of the second linked list, 
then they are intersecting. 

1. problem : 
    is the intersection must be continued?
    yes, because as long as these 2 lists have the same node, then from there on,
    must share all the left nodes, because the first common node can not point to two different next 
2. input: empty list? node 
3. output: data type? Node, if no intersection, then None 
4. edge cases:
5. Time complexity
6. Space complexity

3 -> 1 -> 5 -> 9
                 -> 7 -> 2 -> 1
     2 -> 4 -> 6
return node 7
"""

from typing import Optional 
from LinkedList import LinkedList, Node

def intersection(list1: LinkedList, list2: LinkedList) -> Optional[Node]:
    # because if there are intersection, the tail part is in common 
    # so, don't loop from the head, loop from list1.node1 and list2.node2
    # time complexity: O(A + B)
    # space complexity: O(1)

    if list1.tail != list2.tail:
        return None 

    node1 = list1.head 
    count1 = 0
    while node1:
        count1 += 1
        node1 = node1.next 

    node2 = list2.head 
    count2 = 0
    while node2:
        count2 += 1
        node2 = node2.next 
    
    gap = max(count1, count2) - min(count1, count2)
    if count1 < count2:
        list1, list2 = list2, list1
    node1 = list1.head 
    for i in range(gap):
        node1 = node1.next

    node2 = list2.head 
    while node1 is not node2:
        node1 = node1.next
        node2 = node2.next 
        


    
"""
3 -> 1 -> 5 -> 9
                 -> 7 -> 2 -> 1
     2 -> 4 -> 6
"""
list1 = LinkedList()
list1.add(3)
list1.add(1)
list1.add(5)
list1.add(9)


list2 = LinkedList()
list2.add(2)
list2.add(4)
list2.add(6)

for v in [7, 2, 1]:
    node = Node(v)
    list1.tail.next = node
    list1.tail = node 

    list2.tail.next = node 
    list2.tail = node 

ret = intersection(list1, list2)
if ret:
    print(ret.value)
