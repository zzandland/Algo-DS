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
        leftMost = root
        while leftMost:
            n = leftMost
            if not n.left:
                break
            while n:
                n.left.next = n.right
                if n.next:
                    n.right.next = n.next.left
                n = n.next
            leftMost = leftMost.left
        return root    