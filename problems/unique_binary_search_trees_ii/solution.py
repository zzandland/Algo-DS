# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def copy(self, n: TreeNode) -> TreeNode:    
        if not n: return n
        cp = TreeNode(n.val)
        cp.left = self.copy(n.left)
        cp.right = self.copy(n.right)
        return cp

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        dp = {}
        def fn(l: int, r: int) -> List[TreeNode]:
            if l == r: return [None]
            if (l, r) not in dp:
                res = []
                for j in range(l, r):
                    tmp = TreeNode(j+1)
                    for ln in fn(l, j):
                        tmp.left = ln
                        for rn in fn(j+1, r):
                            tmp.right = rn
                            res.append(self.copy(tmp))
                dp[l, r] = res
            return dp[l, r]
        return fn(0, n)