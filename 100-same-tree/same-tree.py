# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Are either or both trees empty?
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return p.val == q.val and left and right