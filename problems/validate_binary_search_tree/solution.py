# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def fn(n: TreeNode, l: int, r: int) -> bool:
            if not n: return True
            if not (l < n.val < r): return False
            if n.left and n.val < n.left.val: return False
            if n.right and n.val > n.right.val: return False
            return fn(n.left, l, n.val) and fn(n.right, n.val, r)
        return fn(root, float('-inf'), float('inf'))