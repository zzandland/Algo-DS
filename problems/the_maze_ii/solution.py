from heapq import heappush, heappop

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze: return 0 
        M, N = len(maze), len(maze[0])
        
        dir_ = ((-1, 0), (0, 1), (1, 0), (0, -1))
        q = [(0, start[0], start[1])]
        seen = {}
        res = []
        
        def roll(y: int, x: int, dir: int) -> List[int]: 
            r, c = dir_[dir]
            ny, nx = y+r, x+c
            d = 0
            while 0 <= ny < M and 0 <= nx < N and maze[ny][nx] != 1:
                y, x = ny, nx
                ny, nx = y+r, x+c
                d += 1
            return [d, y, x]
        
        while q:
            d, y, x = heappop(q)
            if [y, x] == destination:
                return d
            if (y, x) not in seen or d < seen[y, x]:
                seen[y, x] = d
                for dir in range(4):
                    nd, ny, nx = roll(y, x, dir)
                    heappush(q, (d+nd, ny, nx))
        return -1