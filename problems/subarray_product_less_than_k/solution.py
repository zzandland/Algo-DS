class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        l = 0
        run = 1
        res = 0
        for r, n in enumerate(nums):
            run *= n
            while l <= r and run >= k:
                run //= nums[l]
                l += 1
            res += r-l+1
        return res