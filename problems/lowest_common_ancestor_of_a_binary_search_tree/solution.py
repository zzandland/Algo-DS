# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val: l, h = p, q
        else: l, h = q, p
        while root:
            if l.val <= root.val <= h.val: return root
            if h.val < root.val: root = root.left
            if l.val > root.val: root = root.right
        return root