class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        mx = mn = 1
        res = float('-inf')
        for n in nums:
            if n == 0: mx = mn = 0
            else:
                nmx, nmn = max(n, mx*n, mn*n), min(n, mx*n, mn*n)
                mx, mn = nmx, nmn
            res = max(res, mx)
        return res