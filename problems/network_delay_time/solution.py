from collections import defaultdict
from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        adj, seen = defaultdict(list), set()
        for u, v, w in times:
            adj[u].append((v, w))
        hp, V = [(0, K)], [float('inf')]*N
        V[K-1] = 0
        while hp and len(seen) < N:
            w, n = heappop(hp)
            if n not in seen:
                seen.add(n)
                for nn, nw in adj[n]:
                    V[nn-1] = min(V[nn-1], V[n-1]+nw)
                    heappush(hp, (V[nn-1], nn))
        return max(V) if len(seen) == N else -1