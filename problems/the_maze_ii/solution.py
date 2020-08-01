from heapq import heappush, heappop

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze: return -1
        M, N = len(maze), len(maze[0])
        dir_ = ((-1, 0), (0, 1), (1, 0), (0, -1))
        def roll(y: int, x: int, d: int) -> List[int]:
            r, c = dir_[d]
            ny, nx = y+r, x+c
            cnt = 0
            while 0 <= ny < M and 0 <= nx < N and maze[ny][nx] != 1:
                cnt += 1
                y, x = ny, nx
                ny, nx = y+r, x+c
            return [cnt, y, x]
        q = [(0, start[0], start[1])]
        seen = {tuple(start): 0}
        while q:
            d, y, x = heappop(q)
            if [y, x] == destination: return d
            for i in range(4):
                nd, ny, nx = roll(y, x, i)
                if (ny, nx) not in seen or seen[ny, nx] > d+nd:
                    seen[ny, nx] = d+nd
                    heappush(q, (d+nd, ny, nx))
        return -1