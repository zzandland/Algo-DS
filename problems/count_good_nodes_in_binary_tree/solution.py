# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def cnt(n: TreeNode, mx: int) -> int:
            if not n: return 0
            res = int(n.val >= mx)
            return res + cnt(n.left, max(mx, n.val)) + cnt(n.right, max(mx, n.val))
        return cnt(root, root.val)