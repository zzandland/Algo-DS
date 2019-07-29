class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * n
        maxans = 1
        dp[0] = 1
        for i in range(1, n):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1        
            maxans = max(maxans, dp[i])
        return maxans    