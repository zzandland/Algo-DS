class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        N = len(grid)
        if N == 1 and grid[0][0] == 0:
            return 1
        if grid[0][0] == 1:
            return -1
        dir_ = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
        q, grid[0][0], res = [(0, 0)], 1, 1
        while q:
            nq = []
            res += 1
            for ny, nx in [[y+r, x+c] for y, x in q for r, c in dir_]:
                if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] == 0:
                    if ny == N-1 and nx == N-1:
                        return res
                    grid[ny][nx] = 1
                    nq.append((ny, nx))
            q = nq
        return -1