class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for v in nums:
            dp.append(max(dp[-3], dp[-2]) + v)
        return max(dp[-2], dp[-1])