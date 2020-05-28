class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N-1
        while l+1 < r:
            m = l + (r-l)//2
            if nums[m-1] < nums[m] and nums[m+1] < nums[m]: return m
            if nums[m-1] < nums[m] < nums[m+1]: l = m
            else: r = m
        return l if nums[l] > nums[r] else r
        print(l, r, m)        