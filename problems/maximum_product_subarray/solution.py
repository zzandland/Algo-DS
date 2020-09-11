class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        mn = mx = res = nums[0]
        for n in nums[1:]:
            nmx = max(mx*n, n, mn*n)
            nmn = min(mn*n, n, mx*n)
            mx, mn = nmx, nmn
            res = max(mx, res)
        return res