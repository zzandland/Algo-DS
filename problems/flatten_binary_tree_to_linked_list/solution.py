# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def fn(n: TreeNode) -> TreeNode:
            if not n: return None
            l, r, ln, rn = n.left, n.right, fn(n.left) if n.left else n, fn(n.right) if n.right else n
            if l: 
                n.left, n.right = None, l
                if r: ln.right = r
                else: return ln
            return rn
        fn(root)