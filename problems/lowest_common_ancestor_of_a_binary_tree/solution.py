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
            lf, rf = dfs(n.left), dfs(n.right)
            if lf and rf: res = n
            elif n in (p, q) and (lf or rf): res = n
            return n in (p, q) or lf or rf
        dfs(root)
        return res