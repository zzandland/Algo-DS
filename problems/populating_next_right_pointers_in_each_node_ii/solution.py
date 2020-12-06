"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        q = [root]
        while q:
            nq = []
            prev = None
            for n in q:
                if prev: prev.next = n
                prev = n
                if n.left: nq.append(n.left)
                if n.right: nq.append(n.right)
            q = nq
        return root