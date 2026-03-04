# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # helper function to check whether two trees are the same
        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # edgecase: both trees are empty
            if p is None and q is None:
                return True
            # edgecase: only one tree is empty
            elif p is None or q is None or p.val != q.val:
                return False
            # recursively check whether the left and right subtrees are the same
            left_check = sameTree(p.left, q.left)
            right_check = sameTree(p.right, q.right)
            # if all conditions are satisfied, return True, else False
            return left_check and right_check
        
        # edgecase: if subtree is empty, this is true by default
        if subRoot is None:
            return True
        # edgecase: if root is empty, this is false by default
        if root is None:
            return False
        # # for the current node, check whether the subTree starts from that node
        # if root.val == subRoot.val:
        #     # if so, check whether the trees are the same
        #     if sameTree(root, subRoot):
        #         # if they're same, return True - we found a subtree!
        #         return True
        # if not, check the left and right subtrees
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
