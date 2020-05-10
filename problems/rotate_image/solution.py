class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N//2):
            l = N-1
            for j in range(i, l-i):
                matrix[i][j], matrix[j][l-i], matrix[l-i][l-j], matrix[l-j][i] = matrix[l-j][i], matrix[i][j], matrix[j][l-i], matrix[l-i][l-j] 