class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        run = 1
            
        for r, n in enumerate(nums):
            run *= nums[r]
            while l <= r and run >= k:
                run //= nums[l]
                l += 1
            if l <= r: res += max(0, r-l+1)
            r += 1
        return res