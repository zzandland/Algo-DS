class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        N, mx = len(nums), 1
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] <= dp[j]: dp[i] += 1
                mx = max(mx, dp[i])
        return mx