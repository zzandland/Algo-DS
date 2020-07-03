from heapq import *

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        arr = sorted([((w / q), q) for w, q in zip(wage, quality)])
        window, tq, res = [], 0, float('inf')
        for r, q in arr:
            tq += q
            heappush(window, -q)
            if len(window) > K: tq += heappop(window)
            if len(window) == K: res = min(res, r * tq)
        return res