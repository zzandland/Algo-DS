class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = n = 0
        N = len(nums)
        while zero < N:
            while zero < N and nums[zero] != 0: zero += 1
            if zero == N: return
            n = zero
            while n < N and nums[n] == 0: n += 1
            if n == N: return 
            nums[zero], nums[n] = nums[n], nums[zero]