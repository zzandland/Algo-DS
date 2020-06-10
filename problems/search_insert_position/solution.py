class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] < target and nums[m+1] >= target:
                return m+1
            if nums[m] < target:
                l = m+1
            else:
                r = m
        return l+1 if nums[l] < target else l