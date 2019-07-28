class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = nums[0]
        mn = mx = r
        for i in range(1, len(nums)):
            candidates = (nums[i], nums[i]*mn, nums[i]*mx)
            mn = min(candidates)
            mx = max(candidates)
            r = max(r, mx)
        return r    