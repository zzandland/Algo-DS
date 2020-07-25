class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target: return True
            if nums[m] == nums[l] == nums[r]: l, r = l+1, r-1
            elif nums[l] <= nums[m]:
                if nums[m] > target and target >= nums[l]: r = m
                else: l = m+1
            else:
                if nums[m] < target and target <= nums[r]: l = m+1
                else: r = m
        return False