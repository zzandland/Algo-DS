from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze: return 0 
        M, N = len(maze), len(maze[0])
        dir_ = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def roll(y: int, x: int, dir: int) -> List[int]:
            d = 0
            r, c = dir_[dir]
            ny, nx = y+r, x+c
            while 0 <= ny < M and 0 <= nx < N and maze[ny][nx] != 1:
                y, x = ny, nx
                ny, nx = y+r, x+c
            return [y, x]
            
        q = deque([start])
        seen = set()
        
        while q:
            y, x = q.popleft()
            if [y, x] == destination: return True
            if (y, x) not in seen:
                seen.add((y, x))
                for dir in range(4):
                    q.append(roll(y, x, dir))
                    
        return False