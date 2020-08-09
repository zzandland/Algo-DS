# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        q = [root]
        while q:
            tmp = []
            nq = []
            for n in q:
                tmp.append(n.val)
                if n.left: nq.append(n.left)
                if n.right: nq.append(n.right)
            res.append(sum(tmp) / len(tmp))
            q = nq
        return res