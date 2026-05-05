# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        dummy = ListNode(next=head)

        # Find the end
        p1, p2 = head, dummy
        
        while n != 0:
            p1 = p1.next
            n -= 1

        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next

        return dummy.next
        
        