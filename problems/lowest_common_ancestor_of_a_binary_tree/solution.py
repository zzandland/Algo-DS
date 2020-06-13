# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        def fn(n: TreeNode) -> bool:
            nonlocal res
            if not n:
                return False
            lf, rf = fn(n.left), fn(n.right)
            if lf or rf:
                if n in (p, q) or lf and rf:
                    res = n
                return True
            return n in (p, q)
        fn(root)
        return res