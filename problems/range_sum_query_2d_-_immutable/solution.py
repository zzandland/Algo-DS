class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix:
            R, C = len(matrix)+1, len(matrix[0])+1
            self.dp = [[0]*C for _ in range(R)]
            for y in range(R-1):
                for x in range(C-1):
                    self.dp[y+1][x+1] = self.dp[y][x+1] + self.dp[y+1][x] - self.dp[y][x] + matrix[y][x]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)