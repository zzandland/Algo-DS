"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def helper(n: Node) -> Node:
            p = None
            while n:
                if n.child:
                    tmp = n.next
                    n.next = n.child
                    n.next.prev = n
                    n.child = None
                    child_tail = helper(n.next)
                    child_tail.next = tmp
                    if tmp: tmp.prev = child_tail
                    n = tmp
                    p = child_tail
                else:
                    p = n
                    n = n.next
            return p
        helper(head)
        return head