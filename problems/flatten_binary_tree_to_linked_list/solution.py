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
        def inorder(n: TreeNode) -> TreeNode:
            if not n: return None
            l, ln, r, rn = n.left, inorder(n.left), n.right, inorder(n.right)
            if l:
                n.right, n.left = l, None
                if r: ln.right = r
            if r: return rn    
            if l: return ln
            return n
        inorder(root)
        return root