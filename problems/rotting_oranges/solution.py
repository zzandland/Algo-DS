class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        q, r = [], 0
        for y in range(R):
             for x in range(C):
                if grid[y][x] == 2:
                    q.append([y, x])
                elif grid[y][x] == 1:
                    r += 1
        if r == 0:
            return 0
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        res = 0
        while q:
            if r == 0:
                return res
            nq = []
            for ny, nx in [[y+r, x+c] for y, x in q for r, c in dir_]:
                if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == 1:
                    r -= 1
                    grid[ny][nx] = 2
                    nq.append([ny, nx])
            res += 1
            q = nq
        return -1