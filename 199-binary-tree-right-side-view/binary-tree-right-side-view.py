from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        # we use level-order bfs traversal
        rightView = []
        queue = deque([root])

        while len(queue) != 0:
            rightView.append(queue[-1].val)
            numLevel = len(queue)
            for _ in range(numLevel):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return rightView