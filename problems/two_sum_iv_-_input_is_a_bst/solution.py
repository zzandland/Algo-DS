# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen, st = set(), [root]
        while st:
            n = st.pop()
            if k - n.val in seen:
                return True
            seen.add(n.val)
            if n.left:
                st.append(n.left)
            if n.right:
                st.append(n.right)
        return False