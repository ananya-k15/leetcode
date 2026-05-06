# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use inorder traversal, it visits the nodes in sorted order
        counter = k
        res = root.val
        
        def dfs(node):
            nonlocal counter, res

            if node is None:
                return

            dfs(node.left)

            if counter == 0:
                return
            counter -= 1
            if counter == 0:
                res = node.val
                return

            dfs(node.right)

        dfs(root)
        return res

            
