class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        R, C = len(grid), len(grid[0])
        def fn(y: int, x: int) -> None:
            grid[y][x] = '0'
            for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y+r, x+c
                if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == '1': fn(ny, nx)
        output = 0            
        for y in range(R):
            for x in range(C):
                if grid[y][x] == '1':
                    output += 1
                    fn(y, x)
        return output            