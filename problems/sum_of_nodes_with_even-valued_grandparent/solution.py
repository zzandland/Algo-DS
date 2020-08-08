# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        if root.val & 1 == 0:
            if root.left:
                if root.left.left: res += root.left.left.val
                if root.left.right: res += root.left.right.val
            if root.right:
                if root.right.left: res += root.right.left.val
                if root.right.right: res += root.right.right.val
        return res + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)