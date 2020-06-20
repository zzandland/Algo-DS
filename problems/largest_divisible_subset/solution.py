class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        N = len(nums)
        nums.sort()
        dp, mxi = [1]*N, N-1
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                if nums[j] % nums[i] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
            mxi = max(mxi, i, key=lambda x: dp[x])
        t, res = dp[mxi], []
        while t > 0:
            if dp[mxi] == t:
                res.append(nums[mxi])
                t -= 1
            mxi += 1
        return res