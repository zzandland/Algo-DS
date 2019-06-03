"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        copy = Node(head.val, None, None)
        copy_map = {head: copy}
        copy_head = None
        while head is not None:
            if head.next is not None:
                if head.next in copy_map:
                    copy.next = copy_map[head.next]
                else:
                    next_node = Node(head.next.val, None, None)
                    copy.next = next_node
                    copy_map[head.next] = next_node
            if head.random is not None:
                if head.random in copy_map:
                    copy.random = copy_map[head.random]
                else:
                    rand_node = Node(head.random.val, None, None)
                    copy.random = rand_node
                    copy_map[head.random] = rand_node                
            if copy_head is None:
                copy_head = copy       
            head = head.next
            copy = copy.next    
        return copy_head     