from collections import Counter, deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if grid:
            R, C, houses, found, empty = len(grid), len(grid[0]), [], False, 0
            for y, row in enumerate(grid):
                for x, cell in enumerate(row):
                    if cell == 1: houses.append((y, x))
            moves = [(deque([houses[i]]), {houses[i]: 0}) for i in range(len(houses))]
            visitCnt, dirs, res = Counter(houses), [(0, 1), (0, -1), (1, 0), (-1, 0)], []
            while empty < len(houses):
                for q, visited in moves:
                    n = len(q)
                    if n == 0: empty += 1
                    for _ in range(n):
                        y, x = q.popleft()
                        for r, c in dirs:
                            ny, nx = y+r, x+c
                            if (0 <= ny < R and 0 <= nx < C and
                                grid[ny][nx] == 0 and (ny, nx) not in visited):
                                visited[(ny, nx)] = visited[(y, x)] + 1
                                visitCnt[(ny, nx)] += 1
                                if visitCnt[(ny, nx)] == len(houses):
                                    res.append(sum([visit[(ny, nx)] for _, visit in moves]))
                                q.append((ny, nx))
            return min(res) if res else -1