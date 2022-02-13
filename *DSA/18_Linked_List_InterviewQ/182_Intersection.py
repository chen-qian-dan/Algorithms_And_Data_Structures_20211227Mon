"""
Linked List Interview Q
Q5: Intersection 
Given two (singly) linked lists, determine if the two lists intersect. 
Return the intersecting node. 
Note that the intersection is defined based on reference, not value. 
That is, if the kth node of the first linked list is the exact same node (by ref) as the jth node of the second linked list, 
then they are intersecting. 

1. problem : 
    is the intersection must be continued?
    yes, because as long as these 2 lists have the same node, then from there on,
    must share all the left over nodes, because the first common node can not point to two different next 
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


from Singly_Linked_List import SinglyLinkedList, Node

def intersection(list1: SinglyLinkedList, list2: SinglyLinkedList):
    # because if there are intersection, the tail part is in common 
    # so, don't loop from the head, loop from list1.node1 and list2.node2
    # time complexity: O(A + B)
    # space complexity: O(1)

    if list1.head is None or list2.head is None:
        return None 

    # find list1, list2 len
    i = 0
    cur = list1.head 
    while cur:
        i += 1
        cur = cur.next 
    len1 = i 

    i = 0
    cur = list2.head
    while cur:
        i += 1
        cur = cur.next 
    len2 = i 

    # find the first possible commond nodes  
    commonLen = min(len1, len2)
    i = 0
    cur1 = list1.head 
    while i < len1 - commonLen:
        i += 1
        cur1 = cur1.next 
    i = 0
    cur2 = list2.head 
    while i < len2 - commonLen:
        i += 1
        cur2 = cur2.next 

    # find the commond node 
    while cur1 is not cur2 and cur1:
        cur1 = cur1.next 
        cur2 = cur2.next 
    
    return cur1 if cur1 else None 


"""
3 -> 1 -> 5 -> 9
                 -> 7 -> 2 -> 1
     2 -> 4 -> 6
"""
list1 = SinglyLinkedList()
list1.add(3)
list1.add(1)
list1.add(5)
list1.add(9)


list2 = SinglyLinkedList()
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
print(ret.val)

