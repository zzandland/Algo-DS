from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        def dfs(n: TreeNode, w: int, h: int) -> None:
            if not n: return
            dic[w].append((n.val, h))
            dfs(n.left, w-1, h+1)
            dfs(n.right, w+1, h+1)
        dfs(root, 0, 0)
        return [[n for n, _ in sorted(dic[w], key=lambda x: x[1])] for w in sorted(dic)]