from collections import deque

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A: return 0
        R, C, dir_, visited, found = len(A), len(A[0]), [(1, 0), (-1, 0), (0, 1), (0, -1)], set(), False
        def getPerim(y: int, x: int) -> List[int]:
            output, cnt = [], 0
            for r, c in dir_:
                ny, nx = y+r, x+c
                if 0 <= ny < R and 0 <= nx < C and A[ny][nx] == 1 and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    cnt += 1
                    output += getPerim(ny, nx)
            if cnt < 4: output += [(y, x)]
            return output
        for y in range(R):
            if found: break
            for x in range(C):
                if A[y][x] == 1 and not found:
                    found = True
                    visited.add((y, x))
                    q = deque(getPerim(y, x))
        d = 0            
        while q:
            l = len(q)
            for _ in range(l):
                y, x = q.popleft()
                for r, c in dir_:
                    ny, nx = y+r, x+c
                    if 0 <= ny < R and 0 <= nx < C and (ny, nx) not in visited:
                        if A[ny][nx] == 1: return d
                        visited.add((ny, nx))
                        q.append((ny, nx))
            d += 1
        return d                