# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # let's say we'll switch p & q such that p < q 
        # then the LCA must satify p < LCA < q 
        # we traverse the tree, moving down left/right
        # depenfing on whether LCA > p, q or LCA < p, q

        low = min(p.val, q.val)
        high = max(p.val, q.val)
        current = root

        while current is not None:
            if current.val >= low and current.val <= high:
                return current
            elif current.val > high:
                current = current.left
            else:
                current = current.right
