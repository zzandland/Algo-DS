# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        def getLeaves(n: TreeNode) -> List[int]:
            if not n: return []
            if not n.left and not n.right: return [n.val] if n != root else []
            return getLeaves(n.left) + getLeaves(n.right)
        # left boundary
        def getLB(n: TreeNode) -> List[int]:
            if not n or not n.left and not n.right: return []
            return [n.val] + (getLB(n.left) if n.left else getLB(n.right))
        # right boundary
        def getRB(n: TreeNode) -> List[int]:
            if not n or (not n.left and not n.right): return []
            return ([n.val] if n != root else []) + (getRB(n.right) if n.right else getRB(n.left))
        lb = [root.val] if not root.left else getLB(root)
        rb = [] if not root.right else getRB(root)
        return lb + getLeaves(root) + rb[::-1]