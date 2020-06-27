class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid: return 0
        N, res = len(grid), 0
        matrix = [[[0]*4 for _1 in range(N*2)] for _2 in range(N*2)]
        dir_ = {
            0: lambda y, x: [(y, x, 1), (y, x, 2), (y-1, x, 3)],
            1: lambda y, x: [(y, x, 0), (y, x, 3), (y, x-1, 2)],
            2: lambda y, x: [(y, x, 0), (y, x, 3), (y, x+1, 1)],
            3: lambda y, x: [(y, x, 1), (y, x, 2), (y+1, x, 0)]
        }
        for r, row in enumerate(grid):
            c = 0
            while c < len(row):
                if row[c] == '\\':
                    a, b = matrix[r*2][c*2], matrix[r*2+1][c*2+1]
                    a[0] = a[2] = b[0] = b[2] = 1
                elif row[c] == '/':
                    a, b = matrix[r*2][c*2+1], matrix[r*2+1][c*2]
                    a[2] = a[3] = b[2] = b[3] = 1
                c += 1
        def dfs(y: int, x: int, z: int) -> None:
            matrix[y][x][z] = 1
            for ny, nx, nz in dir_[z](y, x):
                if 0 <= ny < N*2 and 0 <= nx < N*2 and not matrix[ny][nx][nz]:
                    dfs(ny, nx, nz)
        for y, row in enumerate(matrix):
            for x, col in enumerate(row):
                for z in col:
                    if not matrix[y][x][z]:
                        res += 1
                        dfs(y, x, z)
        return res