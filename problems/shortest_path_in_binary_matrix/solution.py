from heapq import heappush, heappop

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1: return -1
        M, N = len(grid), len(grid[0])
        q = [(1, 0, 0)]
        dir_ = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
        seen = {(0, 0): 1}
        while q:
            d, y, x = heappop(q)
            if y == M-1 and x == N-1: return d
            for ny, nx in (((y+r, x+c) for r, c in dir_)):
                if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == 0:
                    if (ny, nx) not in seen or seen[ny, nx] > d+1:
                        seen[ny, nx] = d+1
                        heappush(q, (d+1, ny, nx))
        return -1