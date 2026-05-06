# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            else:
                return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        stack = [root]

        while stack != []:
            node = stack.pop()
            if node is None:
                continue
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            stack.append(node.left)
            stack.append(node.right)

        return False