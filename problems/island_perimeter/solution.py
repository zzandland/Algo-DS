class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        M, N = len(grid), len(grid[0])
        seen = set()
        def dfs(y: int, x: int) -> int:
            if (y, x) in seen: return 0
            seen.add((y, x))
            res = 0
            for ny, nx in [(y+r, x+c) for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1))]:
                if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == 1:
                    res += dfs(ny, nx)
                else:
                    res += 1
            return res
        for y in range(M):
            for x in range(N):
                if grid[y][x] == 1: return dfs(y, x)