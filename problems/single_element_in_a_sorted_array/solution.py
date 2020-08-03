class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums)-1
        while l+1 < r:
            m = l + (r-l)//2
            if nums[m-1] == nums[m]:
                if r-m & 1 == 1: l = m+1
                else: r = m-2
            elif nums[m] == nums[m+1]:
                if m-l & 1 == 1: r = m-1
                else: l = m+2
            else: return nums[m]
        return nums[l]