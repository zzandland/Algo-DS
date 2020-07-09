# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        lefts, res = {}, 0
        def dfs(n: TreeNode, i: int, h: int) -> int:
            if not n: return 0
            lefts.setdefault(h, i)
            lefts[h] = min(lefts[h], i)
            return max(i - lefts[h] + 1, dfs(n.left, i*2, h+1), dfs(n.right, i*2+1, h+1))
        return dfs(root, 0, 1)