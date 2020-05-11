import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hp, root, merged, cnt = [], None, None, 0
        for lst in lists:
            if lst: 
                heapq.heappush(hp, (lst.val, cnt, lst))
                cnt += 1
        while hp:
            _, cnt, n = heapq.heappop(hp)
            tmp = n
            n, tmp.next = n.next, None
            if n: heapq.heappush(hp, (n.val, cnt, n))
            if merged: merged.next = tmp
            merged = tmp    
            if not root: root = merged
        return root        