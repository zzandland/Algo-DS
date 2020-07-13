from heapq import heappush, heappop

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        M, N = len(grid), len(grid[0])
        dir_ = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        
        seen = set()
        
        def dfs(y: int, x: int) -> bool:
            if y == M-1 and x == N-1: return True
            if not (0 <= y < M) or not (0 <= x < N) or (y, x) in seen: return False
            seen.add((y, x))
            iq.add((y, x))
            r, c = dir_[grid[y][x]]
            return dfs(y+r, x+c) 
            
        q = set([(0, 0)])
        cost = 0
        while q:
            iq = set()
            for y, x in q:
                if dfs(y, x): return cost
            nq = set()
            for y, x in iq:
                for d in dir_:
                    if d != grid[y][x]:
                        r, c = dir_[d]
                        ny, nx = y+r, x+c
                        if 0 <= ny < M and 0 <= nx < N:
                            nq.add((ny, nx))
            q = nq
            cost += 1