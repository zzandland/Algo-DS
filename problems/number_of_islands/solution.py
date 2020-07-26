class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        M, N = len(grid), len(grid[0])
        
        res = 0
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # dfs to visit all connected lands O(grid)
        def dfs(y: int, x: int) -> None:
            for ny, nx in ((y+r, x+c) for r, c in dir_):
                if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == '1':
                    grid[ny][nx] = '0'
                    dfs(ny, nx)
        
        # iterate all cells and visit if not visited O(grid)
        for y in range(M):
            for x in range(N):
                if grid[y][x] == '1':
                    res += 1
                    dfs(y, x)
        return res