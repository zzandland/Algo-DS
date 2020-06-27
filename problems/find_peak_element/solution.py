class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 0, len(nums)-1
        while l + 1 < r:
            m = l + (r-l)//2
            if nums[m-1] < nums[m] and nums[m+1] < nums[m]: return m-1
            if nums[m-1] < nums[m]: l = m
            else: r = m
                