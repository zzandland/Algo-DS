# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def fn(a: TreeNode, b: TreeNode) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val == b.val:
                if fn(a.left, b.left) and fn(a.right, b.right):
                    return True
            if b == t:
                return fn(a.left, t) or fn(a.right, t)
            return False
        return fn(s, t)