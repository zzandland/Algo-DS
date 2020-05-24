# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        mx = 0
        def dfs(n: TreeNode) -> int:
            nonlocal mx
            if not n: return 0
            l, r = dfs(n.left), dfs(n.right)
            mx = max(mx, l+r)
            return 1 + max(l, r)
        dfs(root)
        return mx