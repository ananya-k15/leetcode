# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # use a modified stack during dfs to keep 
        # track of max element seen so far
        stack = [[root, root.val]]
        good = 0

        while stack != []:
            node, maxSoFar = stack.pop()
            if node.val >= maxSoFar:
                good += 1
                maxSoFar = node.val
            if node.left is not None:
                stack.append([node.left, maxSoFar])
            if node.right is not None:
                stack.append([node.right, maxSoFar])

        return good
