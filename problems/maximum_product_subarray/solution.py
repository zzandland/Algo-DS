class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        res = float('-inf')
        mx = mn = 0
        for n in nums:
            nmx = max(mx*n, mn*n, n)
            nmn = min(mx*n, mn*n, n)
            mx, mn = nmx, nmn
            res = max(res, mx)
        return res