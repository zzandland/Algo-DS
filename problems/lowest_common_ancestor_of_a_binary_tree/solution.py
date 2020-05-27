# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def dfs(n: TreeNode) -> bool:
            nonlocal lca
            if not n: return False
            ln, rn = dfs(n.left), dfs(n.right)
            if n == p or n == q:
                if ln or rn: lca = n
                return True
            if ln and rn: lca = n
            return ln or rn
        dfs(root)
        return lca