from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edgecase: empty tree
        if root is None:
            return []

        # We need to find the level order of the tree
        # then parse that ordering to return all the right most elements, i.e., -1 indices

        # we use bfs to find the level order
        # master list to store the levels
        rightSideView = []

        # create a queue to store nodes during traversal
        queue = deque([ root ])

        # the bfs algorithm runs until the queue is empty
        while len(queue) > 0:
            # during each iteration of the while loop, num of elements in the queue = number of nodes in the level
            numLevelNodes = len(queue)
            level = []
            # so we keep poping elements until all the nodes of this level are traversed
            while numLevelNodes > 0:
                # and we add them all to a sublist for this level
                node = queue.popleft()
                level.append(node.val)
                # add the children node to the queue (for the next level)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                numLevelNodes -= 1
            # add the sublist to the master levelOrder list
            rightSideView.append(level[-1])

        # parse the levelOrder list to get the rightmost element at each level
        # rightSideView = [x[-1] for x in levelOrder]
        # return the "right side view"
        return rightSideView
