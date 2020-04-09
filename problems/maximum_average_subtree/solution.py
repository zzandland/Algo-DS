# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Tuple

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        mxAvg = 0
        def fn(n: TreeNode) -> Tuple[int, int]:
            nonlocal mxAvg
            if not n: return (0, 0)
            lSum, lCnt = fn(n.left)
            rSum, rCnt = fn(n.right)
            sum_, cnt = n.val + lSum + rSum, lCnt + rCnt + 1
            mxAvg = max(mxAvg, sum_ / cnt)
            return (sum_, cnt)
        fn(root)
        return mxAvg