class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0]*target
        for i, n in enumerate(nums):
            for j in range(n, target+1):
                dp[j] = sum([dp[j-nums[k]] for k in range(i+1)])
        return dp[-1]