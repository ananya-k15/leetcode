import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # the default range is between -infinity, infinity
        MAX, MIN = math.inf, -math.inf
        # a stack to store all the nodes
        stack = [[root, [MIN, MAX]]]
        # until the stack is empty
        while stack != []:
            # check if the node satisfies conditions 1 and 2
            node, valid = stack.pop()
            if node.val <= valid[0] or node.val >= valid[1]:
                return False
            # if the left subtree exists, is it's value less than the current node's value?
            if node.left is not None:
                # form a custom range for the nodes in the left subtree
                customRange = [valid[0], node.val] 
                # add the left child to the stack with the custom range
                stack.append([node.left, customRange])
            # if the right subtree exists, is it's value greater than the current node's value?
            if node.right is not None:
                customRange = [node.val, valid[1]]
                stack.append([node.right, customRange])
        return True




