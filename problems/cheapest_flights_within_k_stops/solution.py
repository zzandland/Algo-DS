from collections import defaultdict
from heapq import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, K: int) -> int:
        adj, q = defaultdict(list), [(0, src, K+1)]
        for u, v, w in flights:
            adj[u].append((v, w))
        while q:
            w, n, k = heappop(q)
            if n == dst:
                return w
            if k > 0:
                for nn, nw in adj[n]:
                    heappush(q, (w+nw, nn, k-1))
        return -1