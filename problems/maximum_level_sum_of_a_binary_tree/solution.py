# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        q, lvs = [root], [float('-inf')]
        while q:
            nq, tmp = [], 0
            for n in q:
                tmp += n.val
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            lvs.append(tmp)
            q = nq
        return max(range(len(lvs)), key=lambda x: lvs[x])