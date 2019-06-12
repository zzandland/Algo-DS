class Solution:
    def exist(self, grid: List[List[str]], match: str) -> bool:
        if len(grid) == 0:
            return False
        if not match:
            return False
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def recurse(r: int, c: int, i: int) -> bool:
            if i == len(match):
                return True
            for row, col in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    if grid[row][col] == match[i] and not visited[row][col]:
                        visited[row][col] = True
                        if recurse(row, col, i + 1):
                            return True
                        visited[row][col] = False
            return False            
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == match[0]:
                    visited[i][j] = True
                    if recurse(i, j, 1):                        
                        return True
                    visited[i][j] = False
        return False            