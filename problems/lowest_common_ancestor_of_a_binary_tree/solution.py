# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(n: TreeNode) -> bool:
            nonlocal res
            if not n: return False
            l, r = dfs(n.left), dfs(n.right)
            if l and r: res = n
            elif (n in (p, q)) and (l or r): res = n
            return n in (p, q) or l or r
        dfs(root)
        return res