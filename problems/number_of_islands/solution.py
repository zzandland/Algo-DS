class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        R, C = len(grid), len(grid[0])
        dir_ = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def fn(y: int, x: int) -> int:
            if not (0 <= y < R and 0 <= x < C) or grid[y][x] == '0': return 0
            grid[y][x] = '0'
            for r, c in dir_:
                fn(y+r, x+c)
            return 1    
        return sum([fn(y, x) for y in range(R) for x in range(C)])