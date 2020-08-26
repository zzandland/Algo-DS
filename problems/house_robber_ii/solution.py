class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def helper(ns: List[int]) -> int:
            dp = [0, 0, 0]
            for n in ns:
                dp.append(max(dp[-3], dp[-2]) + n)
            return max(dp[-1], dp[-2])
        return max(helper(nums[:-1]), helper(nums[1:]))