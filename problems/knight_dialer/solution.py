from functools import lru_cache

class Solution:
    def knightDialer(self, n: int) -> int:
        adj = { 0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 5: (), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4) }
        
        q = [1]*10
        for _ in range(1, n):
            nq = []
            for i in range(10):
                nq.append(sum([q[nxt] for nxt in adj[i]]))
            q = nq
        return sum(q) % (10**9 + 7)