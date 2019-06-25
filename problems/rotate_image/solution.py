class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        off = n - 1
        for i in range(round(n/2)):
            for j in range(i, off-i):
                matrix[i][j], matrix[off-j][i], matrix[off-i][off-j], matrix[j][off-i] = matrix[off-j][i], matrix[off-i][off-j], matrix[j][off-i], matrix[i][j]