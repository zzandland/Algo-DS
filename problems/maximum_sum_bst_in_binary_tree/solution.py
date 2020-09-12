# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0
        empty = [float('inf'), float('inf'), float('inf')]
        fail = [float('-inf'), float('-inf'), float('-inf')]
        def helper(n: TreeNode) -> (int, int, int):
            nonlocal res
            if not n: return empty
            left, right = helper(n.left), helper(n.right)
            if left[0] == float('-inf') or right[0] == float('-inf'): return fail
            sm = l = r = n.val
            if left != empty:
                if left[1] >= n.val: return fail
                sm += left[2]
                l = left[0]
            if right != empty:
                if right[0] <= n.val: return fail
                sm += right[2]
                r = right[1]
            res = max(res, sm)
            return (l, r, sm)
        helper(root)
        return res