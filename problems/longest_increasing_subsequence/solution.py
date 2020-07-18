import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = []
        for i in range(N):
            l, r = 0, len(dp)
            while l < r:
                m = l + (r-l)//2
                if dp[m] < nums[i]: l = m+1
                else: r = m
            if l == len(dp): dp.append(nums[i])
            else: dp[l] = nums[i]
        return len(dp)