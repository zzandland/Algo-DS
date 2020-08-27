# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')
        def dfs(n: TreeNode) -> int:
            nonlocal res
            if not n: return 0
            l, r = dfs(n.left), dfs(n.right)
            res = max(res, n.val+l+r, n.val+l, n.val+r, n.val)
            return max(n.val + max(l, r), n.val)
        dfs(root)
        return res