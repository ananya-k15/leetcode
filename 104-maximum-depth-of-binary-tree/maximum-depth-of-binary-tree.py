# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # if the tree is empty or has no children, return 0/1
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1

        # get depth of left subtree
        left = self.maxDepth(root.left)
        # get depth of right subtree
        right = self.maxDepth(root.right)
        # return max of those + 1
        return 1 + max(left, right)