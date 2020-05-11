import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        res, qs, hp = float('inf'), 0, []
        for r, q in workers:
            heapq.heappush(hp, -q)
            qs += q
            if len(hp) > K: qs += heapq.heappop(hp)
            if len(hp) == K: res = min(res, r*qs)    
        return res