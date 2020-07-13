from heapq import heappush, heappop

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        if not maze: return 'impossible'
        M, N = len(maze), len(maze[0])
        dir_ = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dirc = ['u', 'r', 'd', 'l']
        
        def roll(y: int, x: int, dir: int) -> List[int]:
            r, c = dir_[dir]
            ny, nx = y+r, x+c
            d = 0
            while 0 <= ny < M and 0 <= nx < N and maze[ny][nx] != 1:
                y, x = ny, nx
                if [y, x] == hole: return [d, y, x]
                d += 1
                ny, nx = y+r, x+c
            return [d, y, x]
        
        q = [(0, '', ball[0], ball[1])]
        seen = {}
        shortest = float('inf')
        res = 'zzzzzzzz'
        
        while q:
            d, s, y, x = heappop(q)
            if [y, x] == hole:
                if d <= shortest:
                    shortest = d
                    if s < res: res = s
                    continue
                else: break
            if (y, x) not in seen or seen[y, x] > d:
                seen[y, x] = d
                for dir in range(4):
                    nd, ny, nx = roll(y, x, dir)
                    heappush(q, (d+nd, s+dirc[dir], ny, nx))
                    
        return res if res != 'zzzzzzzz' else 'impossible'