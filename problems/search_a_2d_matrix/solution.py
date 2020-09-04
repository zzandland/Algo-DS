class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False 
        N, M = len(matrix), len(matrix[0])
        
        y, x = N-1, 0
        while y >= 0 and x < M:
            val = matrix[y][x]
            if val == target: return True
            if val < target: x += 1
            else: y -= 1
        return False