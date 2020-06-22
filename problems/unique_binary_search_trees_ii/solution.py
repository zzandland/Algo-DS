from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def copy(self, n: TreeNode) -> TreeNode:
        if not n:
            return None
        res = TreeNode(n.val)
        res.left = self.copy(n.left)
        res.right = self.copy(n.right)
        return res
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        dp = {}
        def dq(l: int, r: int) -> List[TreeNode]:
            if l > r:
                return [None]
            if (l, r) not in dp:
                dp[l, r] = []
                for i in range(l, r+1):
                    n = TreeNode(i)
                    left, right = dq(l, i-1), dq(i+1, r)
                    for ln in left:
                        n.left = ln
                        for rn in right:
                            n.right = rn
                            dp[l, r].append(self.copy(n))
            return dp[l, r]
        return dq(1, n)