# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # we'll use dfs to track the maximum depth
        # stack to store (node, depth)
        stack = [(root, 1)]
        mDepth = 0
        while stack != []:
            node, depth = stack.pop()
            if node.left is not None:
                stack.append((node.left, depth+1))
            if node.right is not None:
                stack.append((node.right, depth+1))
            if depth > mDepth:
                mDepth = depth

        return mDepth
        
        
