# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Start a new list
        head = node = ListNode()

        # Keep going until one of the lists end
        while list1 and list2:
            # At each iteration, compare the current node values for both lists
            # Append and progress in the list with the lower value
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        node.next = list1 or list2

        return head.next

        