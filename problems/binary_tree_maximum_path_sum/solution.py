# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        mx = float('-inf')
        def fn(n: TreeNode) -> int:
            nonlocal mx
            if not n: return 0
            l, r = fn(n.left), fn(n.right)
            mx = max(mx, n.val, n.val+l, n.val+r, n.val+l+r)
            return max(n.val, n.val + max(l, r))
        fn(root)
        return mx