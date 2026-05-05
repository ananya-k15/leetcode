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

        # Find the end of the list using slow/fast pointers
        mid, end = head, head
        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next

        # Sever the two lists
        head2 = mid.next
        mid.next = None

        # Reverse the second half of the linked list
        prev, curr = None, head2
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        head2 = prev

        # Merge the two lists
        while head2:
            temp1, temp2 = head.next, head2.next
            head.next = head2
            head2.next = temp1
            head, head2 = temp1, temp2

        # dummy = mlist = ListNode()
        # flip = 1
        # while list1 and list2:
        #     if flip == 1:
        #         mlist.next = list1
        #         list1 = list1.next
        #         flip = 0
        #     else:
        #         mlist.next = list2
        #         list2 = list2.next
        #         flip = 1
        #     mlist = mlist.next
        # mlist.next = list1 or list2