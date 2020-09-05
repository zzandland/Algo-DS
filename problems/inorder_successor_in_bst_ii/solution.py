"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            right = node.right
            while right.left:
                right = right.left
            return right
        else:
            pr = node.parent
            while pr and pr.right == node:
                node, pr = pr, pr.parent
            return pr
        return None