class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if nums[0] > nums[-1]:
            l, r = 0, len(nums)-1
            while l < r:
                m = l + (r-l)//2
                if nums[m] > nums[m+1]: l = r = m+1
                elif nums[m] > nums[0]: l = m+1
                else: r = m
            if target <= nums[-1]: l, r = l, len(nums)-1
            else: l, r = 0, l-1
        else: l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target: return m
            if nums[m] < target: l = m+1
            else: r = m-1
        return -1