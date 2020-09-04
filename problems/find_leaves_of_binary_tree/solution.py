# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        def removeLeaves(n: TreeNode, tmp: [int]) -> TreeNode:
            if not n.left and not n.right:
                tmp.append(n.val)
                return None
            if n.left: n.left = removeLeaves(n.left, tmp)
            if n.right: n.right = removeLeaves(n.right, tmp)
            return n
        while root:
            tmp = []
            root = removeLeaves(root, tmp)
            res.append(tmp)
        return res