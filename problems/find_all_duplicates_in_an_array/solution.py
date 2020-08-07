class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        N = len(nums)
        while i < N:
            j = nums[i] - 1
            if i != j and nums[j] != j+1: nums[i], nums[j] = nums[j], nums[i]
            else: i += 1
                
        return [n for i, n in enumerate(nums) if n-1 != i]