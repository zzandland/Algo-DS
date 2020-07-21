from collections import deque

class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        N = len(bulbs)
        # convert day as index and pos as value into pos as index and day as value
        slots = [0]*N
        for i, pos in enumerate(bulbs):
            slots[pos-1] = i
            
        if K == 0: return min((max(a, b) for a, b in zip(slots, slots[1:]))) + 1
            
        q = deque()
        l, r = 0, K+1
        if r >= N: return -1
        
        for i in range(r):
            while q and q[-1][0] > slots[i]: q.pop()
            q.append((slots[i], i))
            
        res = float('inf')
        while r < len(bulbs):
            target = max(slots[l], slots[r])
            while q and q[0][1] <= l: q.popleft()
            if q and q[0][0] > target: res = min(res, target + 1)
            while q and q[-1][0] > slots[r]: q.pop()
            q.append((slots[r], r))
            l += 1
            r += 1
        return res if res != float('inf') else -1