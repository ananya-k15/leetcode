# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Use slow and fast pointers to find the midpoint
        slow = fast = head
        while fast and fast.next:
            print("here")
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        # Reverse the second half of the list 
        prev, curr = None, mid
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        head2 = prev
        # Then merge the two lists until both halves are exhausted
        while head2:
            temp1, temp2 = head.next, head2.next
            head.next = head2
            head2.next = temp1
            head, head2 = temp1, temp2
