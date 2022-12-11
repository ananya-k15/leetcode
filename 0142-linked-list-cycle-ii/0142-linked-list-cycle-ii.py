# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pos = -1
        l = []
        while head != None :
            for i in range(0, len(l), 1) : 
                if l[i] == head : 
                    return l[i]
            l.append(head)
            head = head.next
        else : 
            return None
        