# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        idx_map = {num: i for i, num in enumerate(inorder)}
        def helper(l: int, r: int) -> TreeNode:
            if l > r: return None
            val = postorder.pop()
            root = TreeNode(val)
            idx = idx_map[val]
            root.right = helper(idx+1, r)
            root.left = helper(l, idx-1)
            return root
        return helper(0, len(inorder)-1)