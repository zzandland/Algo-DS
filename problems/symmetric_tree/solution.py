# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def helper(l: TreeNode, r: TreeNode) -> bool:
            if not l and not r: return True
            if l and r:
                if l.val != r.val: return False
                return helper(l.right, r.left) and helper(l.left, r.right)
            return False
        return helper(root.left, root.right)