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
        ans = []
        lv = 0
        while q:
            nq, tmp = [], []
            for n in q:
                tmp.append(n.val)
                if n.left: nq.append(n.left)
                if n.right: nq.append(n.right)
            if lv & 1 == 1: tmp = tmp[::-1]
            ans.append(tmp)
            q = nq
            lv += 1
        return ans