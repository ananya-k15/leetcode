# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Use DFS or recursion to compute height
        # At each node, check if difference in heights > 1
        # If yes, return false
        # If not, return true after DFS is done
        balanced = True

        def dfsHeight(root: Optional[TreeNode]) -> int:
            nonlocal balanced

            if root is None:
                return 0
            
            # compute height of left and right subtrees
            lh = dfsHeight(root.left)
            rh = dfsHeight(root.right)

            if abs(lh - rh) > 1:
                balanced = False

            return 1 + max(lh, rh)

        dfsHeight(root)

        return balanced
            
