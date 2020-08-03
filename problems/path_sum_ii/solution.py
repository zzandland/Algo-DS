# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(n: TreeNode, run: int, tmp: List[int]) -> List[List[int]]:
            if not n: return []
            if not n.left and not n.right: return [tmp[:] + [n.val]] if run + n.val == sum else []
            tmp.append(n.val)
            run += n.val
            res = dfs(n.left, run, tmp) + dfs(n.right, run, tmp)
            tmp.pop()
            return res
        return dfs(root, 0, [])