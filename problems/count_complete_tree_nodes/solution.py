# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def getDepth(root: TreeNode) -> int:
            if root is None:
                return 0
            return 1 + getDepth(root.left)
        l_depth = getDepth(root.left)
        r_depth = getDepth(root.right)
        if l_depth == r_depth:
            return pow(2, l_depth) + self.countNodes(root.right)
        else:
            return pow(2, r_depth) + self.countNodes(root.left)