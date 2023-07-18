To find the second-to-last node in a singly linked list: 
- Acess the head list, continuously following the "next" nodes. 
- When the next node's next is None, you have found the second-to-last node. 

To concatenate two singly linked lists, L and M, into a single list N, given only references to the first node of each list: 
- Access the head node of L. Create a new head node for N and point it at the same address as head of L. N's next node will reference L's next node, and so on until L.next equals None. 
- Then, N.next should reference the same element as M.first_element. Follow the trail of M nodes until M.next equals None. 
- L.next of last node should equal None.

A recursive algorithm that counts the number of nodes in a SLL:
- If Node.next = None, return 1. 
- Else, return 1 + count(Node.next) 

To swap two nodes, x and y, in a SLL *L*, given references only to x and y: 
- temp = x.next
- x.next = y.next 
- y.next = temp

To swap two nodes, x and y, in a DLL *L*, given references only to x and y: 
- temp = x.next
- x.next = y.next
- y.next = temp
- temp = x.prev
- x.prev = y.prev
- y.prev = temp