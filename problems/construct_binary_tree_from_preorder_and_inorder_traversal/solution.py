# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idx_map = {num: i for i, num in enumerate(inorder)}
        reverse = preorder[::-1]
        def helper(l: int, r: int) -> TreeNode:
            if l > r: return None
            val = reverse.pop()
            res = TreeNode(val)
            idx = idx_map[val]
            res.left = helper(l, idx-1)
            res.right = helper(idx+1, r)
            return res
        return helper(0, len(inorder)-1)