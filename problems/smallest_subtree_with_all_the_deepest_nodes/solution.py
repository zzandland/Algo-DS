# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(n: TreeNode) -> TreeNode:
            if not n: return (None, 0)
            l, r = dfs(n.left), dfs(n.right)
            if l[1] > r[1]: return (l[0], l[1]+1)
            if l[1] < r[1]: return (r[0], r[1]+1)
            return (n, l[1]+1)
        return dfs(root)[0]