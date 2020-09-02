class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        mx = max(nums)
        l, r = 1, mx+1
        while l < r:
            m = l + (r-l)//2
            if sum([ceil(n / m) for n in nums]) <= threshold: r = m
            else: l = m+1
        return max(l, r)