from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        c = Counter()
        def dfs(n: TreeNode) -> int:
            if not n.left and not n.right:
                c[n.val] += 1
                res = 1 if sum([1 for i in c.values() if i % 2 == 1]) in (0, 1) else 0
                c[n.val] -= 1
                return res
            res = 0
            c[n.val] += 1
            if n.left:
                res += dfs(n.left)
            if n.right:
                res += dfs(n.right)
            c[n.val] -= 1
            return res
        return dfs(root)