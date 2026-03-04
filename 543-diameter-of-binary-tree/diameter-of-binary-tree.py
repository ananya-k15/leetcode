# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # to store diameter value
        self.diameter = 0
        
        # returns height of tree, and computes diameter in the process
        def height(root: Optional[TreeNode]) -> int:
            
            # edgecase: empty tree
            # since we automatically count each subtree, 
            # we use -1 to correct that assumption when the tree does not exist
            if root is None:
                return -1

            # otherwise, find height of left and right subtrees
            lh = height(root.left)
            rh = height(root.right)

            # find current height
            current_height = 1 + max(lh, rh)

            # diameter formed by passing through this root node
            diameter = lh + rh + 2
            self.diameter = max(self.diameter, diameter)

            return current_height
            
        height(root)
        return self.diameter