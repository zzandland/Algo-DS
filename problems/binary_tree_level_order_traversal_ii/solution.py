# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, q = [], [root]
        while q:
            res.append(map(lambda x: x.val, q))
            nq = []
            for n in q:
                if n.left: nq.append(n.left)
                if n.right: nq.append(n.right)
            q = nq
        return res[::-1]