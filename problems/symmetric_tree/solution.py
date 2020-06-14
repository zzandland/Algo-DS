# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def fn(l: TreeNode, r: TreeNode) -> bool:
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and fn(l.left, r.right) and fn(l.right, r.left)
        return fn(root.left, root.right)