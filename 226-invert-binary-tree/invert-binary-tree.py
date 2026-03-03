# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # edge case: empty tree
        if root == None:
            return root
        
        # invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # swap the left and right subtrees
        temp = root.left 
        root.left = root.right
        root.right = temp

        # return the root
        return root