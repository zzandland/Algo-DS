# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()
        def dfs(n: TreeNode) -> bool:
            if not n: return False
            if k - n.val in seen: return True
            seen.add(n.val)
            return dfs(n.left) or dfs(n.right)
        return dfs(root)