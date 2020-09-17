"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dp = {}
        def dfs(n: Node, d: int) -> None:
            if not n: return
            if d in dp: dp[d].next = n
            dp[d] = n
            dfs(n.left, d+1)
            dfs(n.right, d+1)
        dfs(root, 0)
        return root