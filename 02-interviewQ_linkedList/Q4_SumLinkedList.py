"""
Sum Linked List
You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the 1's digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list. 

list1 = 7 -> 1 -> 6     617
list2 = 5 -> 9 -> 2     295
617 + 295 = 912  
output: 2 -> 1 -> 9

1. problem 
2. input: empty list? no 
3. output
4. edge cases
5. time complexity
6. space complexity 
"""

from LinkedList import LinkedList, Node 


def SumLinkedList(list1: LinkedList, list2: LinkedList) -> LinkedList:
    # loop lst, times 10 each each next
    # sum two values up
    # // 10, add the remaind at the end of the ret list 
    timer = 1
    node: Node = list1.head 
    sum: int = node.value * timer
    while node.next:
        node = node.next
        timer *= 10 
        sum += node.value * timer

    timer = 1
    node: Node = list2.head 
    sum += node.value * timer
    while node.next:
        node = node.next
        timer *= 10 
        sum += node.value * timer

    # create return list 
    sum, remaind = divmod(sum, 10)
    ll = LinkedList()
    ll.add(remaind)
    while sum > 0:
        sum, remaind = divmod(sum, 10)
        ll.add(remaind)
    return ll 

list1 = LinkedList()
list1.add(7)
list1.add(1)
list1.add(6)

list2 = LinkedList()
list2.add(5)
list2.add(9)
list2.add(2)

print(SumLinkedList(list1, list2))
