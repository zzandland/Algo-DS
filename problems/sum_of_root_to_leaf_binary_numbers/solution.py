# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(n: TreeNode, tmp: [int]) -> int:
            if not n.left and not n.right: return int(''.join(tmp), 2)
            res = 0
            if n.left:
                tmp.append(str(n.left.val))
                res += dfs(n.left, tmp)
                tmp.pop()
            if n.right:
                tmp.append(str(n.right.val))
                res += dfs(n.right, tmp)
                tmp.pop()
            return res
        return dfs(root, [str(root.val)])