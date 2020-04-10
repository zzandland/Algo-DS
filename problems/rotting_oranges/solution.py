from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        R, C = len(grid), len(grid[0])
        q, left = deque(), set()
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 2: q.append((y, x))
                if cell == 1: left.add((y, x))
        t = rotCnt = 0
        dir_ = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while left and q:
            t += 1            
            l, rotCnt = len(q), 0
            for _ in range(l):
                y, x = q.popleft()
                for v, h in dir_:
                    ny, nx = y+v, x+h
                    if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == 1: 
                        rotCnt += 1
                        left.remove((ny, nx))
                        grid[ny][nx] = 2
                        q.append((ny, nx))
        return -1 if left else t