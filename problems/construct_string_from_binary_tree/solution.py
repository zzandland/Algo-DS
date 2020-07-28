# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ''
        res = str(t.val)
        if not t.left and not t.right: return res
        res += '(' + self.tree2str(t.left) + ')'
        if t.right: res += '(' + self.tree2str(t.right) + ')'
        return res