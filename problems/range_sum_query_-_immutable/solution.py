class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.dp = [0]*N
        for i, n in enumerate(nums):
            self.dp[i] = self.dp[i-1] + n

    def sumRange(self, i: int, j: int) -> int:
        if i == 0: return self.dp[j]
        return self.dp[j] - self.dp[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)