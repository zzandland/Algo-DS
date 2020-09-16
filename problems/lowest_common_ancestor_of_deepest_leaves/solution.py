# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        res, depth = None, -1
        def dfs(n: TreeNode, d: int) -> int:
            nonlocal res, depth
            if not n: return -1
            l, r = dfs(n.left, d+1), dfs(n.right, d+1)
            if l == -1 and r == -1:
                if d > depth:
                    depth = d
                    res = n
                return d
            if l == r and l >= depth:
                depth = l
                res = n
            return max(d, l, r)
        dfs(root, 0)
        return res