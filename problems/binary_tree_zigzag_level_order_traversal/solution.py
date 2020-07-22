# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = [root]
        res = []
        lv = 0
        while q:
            nq = []
            tmp = []
            for n in q:
                tmp.append(n.val)
                if n.left: nq.append(n.left)
                if n.right: nq.append(n.right)
            q = nq
            if lv & 1 == 1: res.append(tmp[::-1])
            else: res.append(tmp)
            lv += 1
        return res