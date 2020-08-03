# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        seen = Counter({0: 1})
        def dfs(n: TreeNode, run: int) -> int:
            if not n: return 0
            run += n.val
            res = seen[run-sum]
            seen[run] += 1
            res += dfs(n.left, run) + dfs(n.right, run)
            seen[run] -= 1
            return res
        return dfs(root, 0)