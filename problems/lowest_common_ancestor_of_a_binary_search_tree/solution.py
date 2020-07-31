# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # make sure that p is always lower
        if q.val < p.val: p, q = q, p
        while root:
            if p.val < root.val < q.val: return root
            if root == p or root == q: return root
            if root.val > q.val: root = root.left
            else: root = root.right
        return root