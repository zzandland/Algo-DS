# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        x_node = None
        def cntP(n: TreeNode) -> int:
            nonlocal x_node
            if not n: return 0
            if n.val == x:
                x_node = n
                return 0
            return 1 + cntP(n.left) + cntP(n.right)
        pcnt = cntP(root)
        lcnt, rcnt = cntP(x_node.left), cntP(x_node.right)
        mx = max(pcnt, lcnt, rcnt)
        return mx + mx > 1 + pcnt + lcnt + rcnt