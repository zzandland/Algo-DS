# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def fn(n: TreeNode, d: int, s: int) -> int:
            if not n: return 0
            if n.left and n.right:
                if ((n.left.val == x and n.right.val == y) or
                    (n.left.val == y and n.right.val == x)):
                    return float('inf')
            if n.val == s: return d
            return max(fn(n.left, d+1, s), (fn(n.right, d+1, s)))
        dx = fn(root, 0, x)
        if dx == float('inf'): return False
        return dx == fn(root, 0, y)