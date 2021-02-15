class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if not len(mat): return []
        pq = [(x.count(1), i) for i, x in enumerate(mat)]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(k)]