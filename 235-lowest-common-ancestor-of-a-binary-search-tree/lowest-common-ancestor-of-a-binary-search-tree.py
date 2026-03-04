# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # We need to compute min(p, q) and max(p, q)
        pq_min = min(p.val, q.val)
        pq_max = max(p.val, q.val)

        # if pq_min > root.value, look in the right subtree
        if pq_min > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # if pq_max < root.value, look in the left subtree
        if pq_max < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # otherwise, pq_min <= root.value <= pq_max
        # the root is the LCA
        return root
