class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        res = float('inf')
        hp = []
        qsum = 0
        for r, q in sorted((w / q, q) for w, q in zip(wage, quality)):
            qsum += q
            heappush(hp, -q)
            if len(hp) > K: qsum += heappop(hp)
            if len(hp) == K: res = min(res, r * qsum)
        return res