# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = [root]
        while q:
            nq, left = [], q[0].val
            for n in q:
                if n.left: nq.append(n.left)
                if n.right: nq.append(n.right)
            q = nq
        return left