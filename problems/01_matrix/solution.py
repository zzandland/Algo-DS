from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        dir_, cnt = ((1, 0), (-1, 0), (0, 1), (0, -1)), -1
        seen, q = [[False]*C for _ in range(R)], deque()
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    q.append((r, c))
                    seen[r][c] = True
        while q:
            cnt += 1
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()
                matrix[r][c] = cnt
                for y, x in dir_:
                    nr, nc = r+y, c+x
                    if 0 <= nr < R and 0 <= nc < C and not seen[nr][nc]:
                        seen[nr][nc] = True
                        q.append((nr, nc))
        return matrix