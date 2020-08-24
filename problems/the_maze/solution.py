from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze: return False
        M, N = len(maze), len(maze[0])
        dir_ = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        def move(y: int, x: int, d: int) -> List[int]:
            ny, nx = y + dir_[d][0], x + dir_[d][1]
            while 0 <= ny < M and 0 <= nx < N and maze[ny][nx] != 1:
                y, x = ny, nx
                ny, nx = y + dir_[d][0], x + dir_[d][1]
            return [y, x]
        q = deque([start])
        seen = set([tuple(start)])
        while q:
            y, x = q.popleft()
            if [y, x] == destination: return True
            for i in range(4):
                ny, nx = move(y, x, i)
                if (y != ny or x != nx) and (ny, nx) not in seen:
                    q.append((ny, nx))
                    seen.add((ny, nx))
        return False