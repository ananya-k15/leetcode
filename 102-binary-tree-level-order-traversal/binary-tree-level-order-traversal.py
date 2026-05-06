from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levelOrder = []
        dq = deque([root])
        
        while len(dq) != 0:
            numLevel = len(dq)
            level = [x.val for x in list(dq) if x is not None]
            if level != []:
                levelOrder.append(level)
            for _ in range(numLevel):
                node = dq.popleft()
                if node is not None:
                    dq.append(node.left)
                    dq.append(node.right)

        return levelOrder