# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(n: TreeNode, sm: int) -> TreeNode:
            sm += n.val
            if not n.left and not n.right: return None if sm < limit else n
            if n.left: n.left = dfs(n.left, sm)
            if n.right: n.right = dfs(n.right, sm)
            if not n.left and not n.right: return None
            return n
        return dfs(root, 0)