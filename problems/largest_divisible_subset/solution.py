class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        
        dp = {}
        for i in range(N):
            dp.setdefault(i, [nums[i]])
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + [nums[i]], key=len)
        return max(dp.values() or [[]], key=len)