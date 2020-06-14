class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N, dp = len(nums), {}
        def dq(i: int, l: int) -> List[int]:
            if i == N:
                return []
            if (i, l) not in dp:
                num = nums[i]
                if l != 0 and num % l == 0 or l % num == 0:
                    dp[i, l] = max([num] + dq(i+1, max(l, num)), dq(i+1, l), key=len)
                else:
                    dp[i, l] = dq(i+1, l)
            return dp[i, l]
        return dq(0, 0)