"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        prev, cur = head, head.next
        rotation = False
        while True:
            if (prev.val <= insertVal <= cur.val or
                (rotation and cur == head) or
                (prev.val > cur.val and (prev.val <= insertVal or insertVal <= cur.val))):
                tmp = Node(insertVal)
                prev.next = tmp
                tmp.next = cur
                return head
            prev, cur = cur, cur.next
            if cur == head: rotation = True