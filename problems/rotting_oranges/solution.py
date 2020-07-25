class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        # count oranges and save coords of rottens O(grid)
        oranges, q = 0, []
        for y in range(M):
            for x in range(N):
                if grid[y][x] == 1: oranges += 1
                elif grid[y][x] == 2: q.append((y, x))
                    
        # rot fresh oranges until no more can be done O(grid)
        time = 0
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while True:
            nq = []
            for y, x in q:
                for ny, nx in ((y+r, x+c) for r, c in dir_):
                    if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == 1:
                        grid[ny][nx] = 2
                        oranges -= 1
                        nq.append((ny, nx))
            q = nq
            if not q: return time if oranges == 0 else -1
            time += 1