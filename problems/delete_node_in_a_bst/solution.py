# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if root.val != key:
            if root.val > key: root.left = self.deleteNode(root.left, key)
            else: root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)
            elif not root.left: return root.right
            else: return root.left
        return root