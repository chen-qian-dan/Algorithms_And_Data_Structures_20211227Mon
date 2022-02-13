"""
Linked List Interview Q
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

from Singly_Linked_List import SinglyLinkedList

def SumLinkedList(list1: SinglyLinkedList, list2: SinglyLinkedList) -> SinglyLinkedList:
    ret = SinglyLinkedList()
    carrier = 0
    
    cur1 = list1.head 
    cur2 = list2.head 
    while cur1 or cur2:
        val1 = cur1.val if cur1 else 0 
        val2 = cur2.val if cur2 else 0

        carrier, remain = divmod((carrier + val1 + val2), 10)
        ret.add(remain)

        cur1 = cur1.next if cur1 else None 
        cur2 = cur2.next if cur2 else None 
    
    if carrier > 0:
        ret.add(carrier)

    return ret 


list1 = SinglyLinkedList()
list1.add(7)
list1.add(1)
list1.add(6)

list2 = SinglyLinkedList()
list2.add(5)
list2.add(9)
list2.add(2)

print(SumLinkedList(list1, list2))