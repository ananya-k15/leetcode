# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # returns [diameter, height] of tree
        def diameterAndHeight(root: Optional[TreeNode]) -> int:
            
            # if tree is empty, return [0, 0]
            if root is None:
                return [0, 0]
            
            # if it's a leaf node, return [0, 1]
            if root.left is None and root.right is None:
                return [0, 0]

            # otherwise, find diameters of left and right subtrees
            ld, lh = diameterAndHeight(root.left)
            rd, rh = diameterAndHeight(root.right)

            # choose max of diameter(left subtree) OR diameter(right subtree)
            # OR diameter formed by including current root node, i.e., 
            # 1 + height of left subtree + height of right subtree
            current_diam = 0
            current_diam += lh + 1 if root.left is not None else 0
            current_diam += rh + 1 if root.right is not None else 0

            current_height = 1 + max(lh, rh)

            max_diam = max(ld, rd, current_diam)

            return [max_diam, current_height]

        return diameterAndHeight(root)[0]