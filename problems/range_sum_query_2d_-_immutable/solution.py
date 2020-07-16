class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for y in range(1, m+1):
            for x in range(1, n+1):
                dp[y][x] = matrix[y-1][x-1] + dp[y-1][x] + dp[y][x-1] - dp[y-1][x-1]
                
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)