# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        output = None
        def DFS(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
            nonlocal output
            if root is None:
                return False
            left_found = DFS(root.left, p, q)
            right_found  = DFS(root.right, p, q)
            if root is p or root is q:
                if left_found or right_found:
                    output = root
                return True
            if left_found and right_found:
                output = root
                return True
            if left_found or right_found:
                return True
            return False
        DFS(root, p, q)
        return output