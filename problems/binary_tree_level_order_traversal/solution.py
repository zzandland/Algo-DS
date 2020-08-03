# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = [root]
        res = []
        while q:
            nq = []
            level = []
            for n in q:
                level.append(n.val)
                if n.left: nq.append(n.left)
                if n.right: nq.append(n.right)
            q = nq       
            res.append(level)
        return res