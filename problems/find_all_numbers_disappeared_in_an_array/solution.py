class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        N = len(nums)
        while i < N:
            j = nums[i]-1
            if nums[i] != nums[j]: nums[i], nums[j] = nums[j], nums[i]
            else: i += 1
        return [i+1 for i in range(N) if nums[i] != i+1]