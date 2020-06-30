class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        remain, dir_ = set(), ((1, 0), (-1, 0), (0, 1), (0, -1))
        for y in range(M):
            for x in range(N):
                if grid[y][x] == 1: start = (y, x)
                elif grid[y][x] == 2: end = (y, x)
                elif grid[y][x] == 0: remain.add((y, x))
        remain.add(end)
        def dfs(y: int, x: int) -> int:
            if (y, x) == end: return int(not remain)
            res = 0
            for ny, nx in [(y+r, x+c) for r, c in dir_]:
                if 0 <= ny < M and 0 <= nx < N and (ny, nx) in remain:
                    remain.remove((ny, nx))
                    res += dfs(ny, nx)
                    remain.add((ny, nx))
            return res
        return dfs(*start)