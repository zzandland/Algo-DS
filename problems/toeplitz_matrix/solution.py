class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        def check(y: int, x: int) -> bool:
            val = matrix[y][x]
            while y < M and x < N:
                if matrix[y][x] != val: return False
                y += 1
                x += 1
            return True
        for y in range(M-1, -1, -1):
            if not check(y, 0): return False
        for x in range(1, N):
            if not check(0, x): return False
        return True