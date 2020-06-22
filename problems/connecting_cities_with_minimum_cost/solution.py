from heapq import *
from collections import defaultdict

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in connections:
            adj[u].append((w, v))
            adj[v].append((w, u))
        seen, q, res = set(), [(0, 1)], 0
        while q and len(seen) < N:
            w, u = heappop(q)
            if u not in seen:
                seen.add(u)
                res += w
                for nw, v in adj[u]:
                    if v not in seen:
                        heappush(q, (nw, v))
        return -1 if len(seen) < N else res