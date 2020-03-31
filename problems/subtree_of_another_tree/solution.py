# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def hashify(n: TreeNode) -> str:
            if not n: return '#'
            return '[{},{},{}]'.format(n.val, hashify(n.left), hashify(n.right))
        t_hashed = hashify(t)
        def traverse(n: TreeNode) -> bool:
            if not n: return False
            if hashify(n) == t_hashed: return True
            return traverse(n.left) or traverse(n.right)
        return traverse(s)