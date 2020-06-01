class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N, res = len(nums), 0
        dp = [float('-inf')]*N
        for num in nums:
            l, r = 0, res-1
            while l < r:
                m = l + (r-l)//2
                if dp[m] == num:
                    l = r = m
                elif dp[m] > num:
                    r = m
                else:
                    l = m+1
            if num > dp[l]:
                dp[res] = num
                res += 1
            else:
                dp[l] = num
        return res