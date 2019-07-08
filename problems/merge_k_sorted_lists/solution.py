# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hp, n, merge, out = [], None, None, None
        for lst in lists:
            if lst:
                heapq.heappush(hp,(lst.val, str(lst), lst))
        while hp:    
            _, s, n = heapq.heappop(hp)    
            tmp = n
            n = n.next
            if n:
                heapq.heappush(hp, (n.val, s, n))
            if merge:
                merge.next = tmp
            merge = tmp    
            if not out:
                out = merge
        return out        