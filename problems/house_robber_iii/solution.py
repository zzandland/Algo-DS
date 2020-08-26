# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        dp = {}
        def dfs(n: TreeNode, visited: bool) -> int:
            if not n: return 0
            if (n, visited) not in dp:
                if visited: dp[n, visited] = dfs(n.left, False) + dfs(n.right, False)
                else:
                    dp[n, visited] = max(
                        n.val + dfs(n.left, True) + dfs(n.right, True),
                        dfs(n.left, False) + dfs(n.right, False)
                    )
            return dp[n, visited]
        return dfs(root, False)