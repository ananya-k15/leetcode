# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # We can use a modified version of DFS to complete this
        # As we explore each path to a node, we can keep track of 
        # the maximum element we've encountered till that node, and 
        # compare any new neighbours to that node's max value

        # create a custom stack that stores [node, max value till that node]
        stack = [[root, root.val]]
        goodNodes = 0

        while stack != []:
            # pop a node from the stack and it's max value so far
            node, maxSoFar = stack.pop()

            # check whether the current node is a good node
            if node.val >= maxSoFar:
                # modify maxSoFar
                maxSoFar = node.val
                goodNodes += 1
            
            # add all children of node to the back of the stack
            if node.left is not None:
                stack.append([node.left, maxSoFar])
            if node.right is not None:
                stack.append([node.right, maxSoFar])

        return goodNodes