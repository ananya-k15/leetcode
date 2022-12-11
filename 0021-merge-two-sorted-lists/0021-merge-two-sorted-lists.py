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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = getList(list1)
        l2 = getList(list2)
        l = l1 + l2
        l.sort()
        return createList(l)
        