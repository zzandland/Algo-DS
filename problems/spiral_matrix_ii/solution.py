class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid, dir_ = [[None for _ in range(n)] for _ in range(n)], [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = y = x = 0
        for i in range(1, n*n+1):
            grid[y][x] = i
            ny, nx = y+dir_[cur_dir][0], x+dir_[cur_dir][1]
            if not (0 <= ny < n and 0 <= nx < n) or grid[ny][nx] != None:
                cur_dir = (cur_dir+1) % 4
                ny, nx = y+dir_[cur_dir][0], x+dir_[cur_dir][1]
            y, x = ny, nx    
        return grid    