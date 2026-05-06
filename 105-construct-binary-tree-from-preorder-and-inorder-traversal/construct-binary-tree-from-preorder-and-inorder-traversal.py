# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base cases
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        # find index of root node
        rootIndex = inorder.index(preorder[0])
        # find inorder traversals of subtrees
        lsInorder = inorder[:rootIndex]
        rsInorder = inorder[rootIndex+1:]
        # find preorder traversals of subtrees
        lsLength = len(lsInorder)
        rsLength = len(rsInorder)
        # recursively find left and right subtrees
        ltree, rtree = None, None
        if lsLength > 0:
            lsPreorder = preorder[1:lsLength+1]
            ltree = self.buildTree(lsPreorder, lsInorder)
        if rsLength > 0:
            rsPreorder = preorder[lsLength+1:]
            rtree = self.buildTree(rsPreorder, rsInorder)
        return TreeNode(preorder[0], ltree, rtree)