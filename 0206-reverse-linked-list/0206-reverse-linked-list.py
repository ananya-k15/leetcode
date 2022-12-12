def getList(nodeList) : 
    l = []
    while (nodeList != None) : 
        l.append(nodeList.val)
        nodeList = nodeList.next
    return l

def createList(l) :
    if (l == []) : 
        return None
    else : 
        return ListNode(l[0], createList(l[1:]))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = getList(head)
        return createList(l[::-1])
        
        