class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set, col_set = set(), set()
        
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    row_set.add(i)
                    col_set.add(j)
                    
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0