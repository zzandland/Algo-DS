from heapq import heappush, heappop

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        if not A: return 0
        M, N = len(A), len(A[0])
        dir_ = (-1, 0, 1, 0, -1)
        q = [(-A[0][0], 0, 0)]
        seen = set([0])
        
        while q:
            v, y, x = heappop(q)
            if y == M-1 and x == N-1: return -v
            for ny, nx in ((y+r, x+c) for r, c in zip(dir_, dir_[1:])):
                if 0 <= ny < M and 0 <= nx < N and (ny*N+nx) not in seen:
                    seen.add(ny*N+nx)
                    heappush(q, (max(v, -A[ny][nx]), ny, nx))
        return -1