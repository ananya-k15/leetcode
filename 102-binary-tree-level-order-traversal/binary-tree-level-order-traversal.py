from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Use BFS
        # edgecase: when the tree is empty
        if root == None:
            return []

        # maintain a queue to keep track of which nodes to visit next
        # initialize queue with the root node
        queue = deque([root])

        # list to keep track of order traversal
        level_order = []

        # while there are nodes in the queue
        while len(queue) != 0:
            # find the number of elements in the queue
            # i.e., the number of elements at that level
            elements = len(queue)
            level = []
    
            # while there are nodes left at this level
            while elements > 0:
                # get the first element from the queue
                node = queue.popleft()

                # for each node, add any children to the queue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

                # add the node's value to the level's list
                level.append(node.val)

                elements -= 1

            # we're done adding elements at this level, 
            # so we can update the master level_order list
            level_order.append(level)

        return level_order