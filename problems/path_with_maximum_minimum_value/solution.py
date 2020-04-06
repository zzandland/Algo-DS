import heapq

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0])
        hp, min_, visited = [(-A[0][0], 0, 0)], A[0][0], [[False for _ in range(col)] for _ in range(row)]
        dir_ = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while True:
            val, y, x = heapq.heappop(hp)
            visited[y][x] = True
            min_ = min(min_, A[y][x])
            if y == row-1 and x == col-1: return min_
            for r, c in dir_:
                ny, nx = y+r, x+c
                if 0 <= ny < row and 0 <= nx < col and not visited[ny][nx]:
                    heapq.heappush(hp, (-A[ny][nx], ny, nx))
        return min_