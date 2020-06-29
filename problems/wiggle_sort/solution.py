class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        grt = True
        for i in range(len(nums)-1):
            if grt and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif not grt and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            grt = not grt