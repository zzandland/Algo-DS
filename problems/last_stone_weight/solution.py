from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = [-s for s in stones]
        heapify(st)
        
        while len(st) > 1:
            new = abs(heappop(st) - heappop(st))
            heappush(st, -new)
        return -st[-1]