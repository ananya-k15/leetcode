"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Interweave the new nodes into the old nodes ll
        curr = head
        while curr:
            temp = curr.next
            curr.next = Node(curr.val, temp, None)
            curr = curr.next.next
        
        rcur = head
        while rcur:
            old = rcur
            new = rcur.next

            rold = old.random
            if rold is None:
                new.random = None
            else:
                new.random = rold.next

            rcur = rcur.next.next

        dum1 = dummy = Node(0)
        while head:
            dummy.next = head.next
            head = head.next.next
            dummy = dummy.next
        
        return dum1.next
