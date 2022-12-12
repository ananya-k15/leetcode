# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy = head
        l = 0
        while copy!=None : 
            l += 1
            copy = copy.next
        middle = l//2
        while middle != 0 : 
            middle -= 1
            head = head.next
        return head