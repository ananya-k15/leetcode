# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:   
        maxDiameter = 0
        # use a helper function to perform dfs 
        def height(node: Optional[TreeNode]) -> None:
            nonlocal maxDiameter
            if node is None:
                return -1

            # at each node, we have two options:
            # either the maxDiameter passes through the current node
            # or the maxDiameter is the height of a subtree, depending on:
            # height(left) + height(right) + 2 > height(left/right) + 1

            lh, rh = height(node.left), height(node.right)
            diameter = max(lh + rh + 2, lh + 1, rh + 1)
            if diameter > maxDiameter:
                maxDiameter = diameter
            return max(lh, rh) + 1

        height(root)
        return maxDiameter


