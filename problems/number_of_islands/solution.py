class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        visited = []
        height = len(grid)
        width = len(grid[0])
        def valid_coord(y: int, x: int) -> bool:
            nonlocal height, width    
            return 0 <= y < height and 0 <= x < width
        output = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    output += 1
                    q = collections.deque()
                    q.append((i, j))
                    grid[i][j] = '0'
                    while len(q) > 0:
                        y, x = q.popleft()
                        if valid_coord(y + 1, x) is True and grid[y + 1][x] == '1':
                            grid[y + 1][x] = '0'
                            q.append((y + 1, x))
                        if valid_coord(y - 1, x) is True and grid[y - 1][x] == '1':
                            grid[y - 1][x] = '0'
                            q.append((y - 1, x))
                        if valid_coord(y, x + 1) is True and grid[y][x + 1] == '1':
                            grid[y][x + 1] = '0'
                            q.append((y, x + 1))
                        if valid_coord(y, x - 1) is True and grid[y][x - 1] == '1':
                            grid[y][x - 1] = '0'
                            q.append((y, x - 1))
        return output                       