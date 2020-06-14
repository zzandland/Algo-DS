from collections import deque
from heapq import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, K: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        q = [(0, src, K+1)]
        while q:
            w, n, k = heappop(q)
            if n == dst and k >= 0:
                return w
            if n != dst and k > 0:
                for nn, nw in adj[n]:
                    heappush(q, (w + nw, nn, k-1))
        return -1