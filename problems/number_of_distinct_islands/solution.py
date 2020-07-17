from typing import Tuple
from collections import deque

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        M, N = len(grid), len(grid[0])
        shapes = set()
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # bfs and store relative pos from where you start O(grid)
        def bfs(y: int, x: int) -> Tuple[Tuple[int, int]]:
            coords, q = [], deque([(y, x)])
            # in each coord try visiting all four directions if land O(grid)
            while q:
                r, c = q.popleft()
                # store relative position from initial y, x
                coords.append((y-r, x-c))
                for nr, nc in [(r+yy, c+xx) for yy, xx in dir_]:
                    if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return tuple(sorted(coords))
            
        res = 0
        # iterate the grid O(grid)
        for y, x in [(y, x) for y in range(M) for x in range(N)]:
            if grid[y][x] == 1:
                grid[y][x] = 0
                # check the shape
                shape = bfs(y, x)
                if shape not in shapes:
                    res += 1
                    shapes.add(shape)
        return res