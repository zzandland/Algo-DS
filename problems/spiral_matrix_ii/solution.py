class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        num, dir_, di = 1, [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        y = x = turn = 0
        py = px = -1
        while turn < 2:
            while 0 <= y < n and 0 <= x < n:
                if res[y][x] != 0:
                    break
                turn = 0
                res[y][x] = num
                num += 1
                py, px = y, x
                y += dir_[di][0]
                x += dir_[di][1]
            turn += 1
            di = (di+1) % 4
            y, x = py + dir_[di][0], px + dir_[di][1]
        return res