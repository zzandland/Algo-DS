# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(n: TreeNode) -> TreeNode:
            if not n: return None
            n.left, n.right = dfs(n.right), dfs(n.left)
            return n
        return dfs(root)
            