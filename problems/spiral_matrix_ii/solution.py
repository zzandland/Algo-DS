class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dir_, di = ((0, 1), (1, 0), (0, -1), (-1, 0)), 0
        matrix = [[0]*n for _ in range(n)]
        y = x = 0
        for i in range(1, n*n+1):
            matrix[y][x] = i
            r, c = dir_[di]
            ny, nx = y+r, x+c
            if not (0 <= ny < n and 0 <= nx < n) or matrix[ny][nx] != 0:
                di = (di+1) % 4
                r, c = dir_[di]
                ny, nx = y+r, x+c
            y, x = ny, nx
        return matrix