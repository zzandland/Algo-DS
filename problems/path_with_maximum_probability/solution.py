from collections import defaultdict, Counter
from heapq import heappush, heappop

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))
        q = [(-1, start)]
        seen = {start: -1}
        while q:
            prob, n = heappop(q)
            if n == end: return -prob
            for nn, crossProb in adj[n]:
                tmp = prob*crossProb
                if nn not in seen or seen[nn] > tmp:
                    seen[nn] = tmp
                    heappush(q, (tmp, nn))
        return 0