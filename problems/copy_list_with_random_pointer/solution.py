"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic, cur = {}, head
        dic[None] = None
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head    
        while cur:
            n = dic[cur]
            n.next = dic[cur.next]
            n.random = dic[cur.random]
            cur = cur.next
        return dic[head]    