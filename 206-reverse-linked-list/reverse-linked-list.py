# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        elif head.next is None:
            return head
        
        n1, n2 = head, head.next
        prev = None
        while True:
            # print(n1.val, n2.val)
            n1.next = prev
            temp = n2.next
            n2.next = n1
            # print(temp, n1.val, n2.val, n1.next, n2.next)
            if temp == None:
                return n2
            else:
                prev = n1
                n1, n2 = n2, temp

        
            

