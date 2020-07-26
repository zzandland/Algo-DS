class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return matrix
        M, N = len(matrix), len(matrix[0])
        seen = set()
        q = []
        
        # get all zeros O(matrix)
        for y in range(M):
            for x in range(N):
                if matrix[y][x] == 0:
                    seen.add((y, x))
                    q.append((y, x))
                    
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # flood-fill all non-zero cells O(matrix)
        cnt = 0
        while q:
            nq = []
            cnt += 1
            for y, x in q:
                for ny, nx in ((y+r, x+c) for r, c in dir_):
                    if 0 <= ny < M and 0 <= nx < N and (ny, nx) not in seen:
                        seen.add((ny, nx))
                        matrix[ny][nx] = cnt
                        nq.append((ny, nx))
            q = nq        
        return matrix