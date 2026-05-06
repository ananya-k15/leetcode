import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        MIN, MAX = -math.inf, math.inf

        # root can be between +ve and -ve infinity
        # left subtree can have values between [parent's left range, parent.val]
        # left subtree can have values between [parent.val, parent's right range]
        # all ranges are non-inclusive

        # dfs with modified stack (contains allowed range of values)
        stack = [[root, MIN, MAX]]

        while stack != []:
            node, low, high = stack.pop()
            if node.val <= low or node.val >= high:
                return False
            if node.left is not None:
                stack.append([node.left, low, node.val])
            if node.right is not None:
                stack.append([node.right, node.val, high])
            
        return True
