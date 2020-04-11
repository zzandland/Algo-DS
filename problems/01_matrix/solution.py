from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix:
            R, C, d, dir_ = len(matrix), len(matrix[0]), -1, [(1, 0), (-1, 0), (0, 1), (0, -1)]
            q = deque([(y, x) for y in range(R) for x in range(C) if matrix[y][x] == 0])
            v = [[matrix[y][x] == 0 for x in range(C)] for y in range(R)]
            while q:
                d+=1
                l = len(q)
                for _ in range(l):
                    y, x = q.popleft()
                    matrix[y][x] = d
                    for r, c in dir_:
                        ny, nx = y+r, x+c
                        if 0 <= ny < R and 0 <= nx < C and not v[ny][nx] and matrix[ny][nx] == 1:
                            v[ny][nx] = True
                            q.append((ny, nx))
        return matrix                