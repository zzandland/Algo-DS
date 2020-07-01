# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root: return 0
        q = [root]
        mx, lv = 0, 0
        while q:
            nq, cur = [], 0
            lv += 1
            for n in q:
                cur += n.val
                if n.left: nq.append(n.left)
                if n.right: nq.append(n.right)
            if cur > mx: mx, res = cur, lv
            q = nq
        return res