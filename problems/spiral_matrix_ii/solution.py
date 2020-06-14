class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dir_, di = ((0, 1), (1, 0), (0, -1), (-1, 0)), 0
        res = [[0]*n for _ in range(n)]
        y = x = 0
        for i in range(1, n*n+1):
            res[y][x] = i
            ny, nx = y + dir_[di][0], x + dir_[di][1]
            if not (0 <= ny < n and 0 <= nx < n and res[ny][nx] == 0):
                di = (di+1) % 4
                ny, nx = y + dir_[di][0], x + dir_[di][1]
            y, x = ny, nx
        return res