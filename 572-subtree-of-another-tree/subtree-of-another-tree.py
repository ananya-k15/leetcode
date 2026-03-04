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
            elif p is None or q is None:
                return False
            # check whether the root values match
            root_check = p.val == q.val
            # recursively check whether the left and right subtrees are the same
            left_check = sameTree(p.left, q.left)
            right_check = sameTree(p.right, q.right)
            # if all conditions are satisfied, return True, else False
            return root_check and left_check and right_check
        
        # edgecase: if both trees are empty, this is true by default
        if root is None and subRoot is None:
            return True
        # edgecase: if root is empty, this is False by default
        elif root is None:
            return False
        # edgecase: if subtree is empty, this is true by default
        elif subRoot is None:
            return True
        # for the current node, check whether the subTree starts from that node
        # if not, check the left and right subtrees
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
