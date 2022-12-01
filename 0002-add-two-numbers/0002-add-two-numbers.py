def addTwoNodes(l1, l2, diff): 
    if ((l1 == None) and (l2 == None)) :
        if (diff == 0):
            return None
        else:
            return ListNode(diff, None)
    elif ((l1 == None) and (l2 != None)) :
        diff += l2.val
        if (diff > 9) :
            return ListNode(diff - 10, addTwoNodes(l2.next, None, 1))
        else :
            return ListNode(diff, addTwoNodes(l2.next, None, 0))
    elif ((l1 != None) and (l2 == None)) :
        diff += l1.val
        if (diff > 9) :
            return ListNode(diff - 10, addTwoNodes(l1.next, None, 1))
        else :
            return ListNode(diff, addTwoNodes(l1.next, None, 0))
    else : 
        diff += l1.val + l2.val
        if (diff > 9) :
            return ListNode(diff - 10, addTwoNodes(l1.next, l2.next, 1))
        else : 
            return ListNode(diff, addTwoNodes(l1.next, l2.next, 0))
    
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        diff = l1.val + l2.val
        if (diff > 9) : 
            return ListNode(diff - 10, addTwoNodes(l1.next, l2.next, 1))
        else :
            return ListNode(diff, addTwoNodes(l1.next, l2.next, 0))
            
            
            
            
            
            
            
            
            
            
            