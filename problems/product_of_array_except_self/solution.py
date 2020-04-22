class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output, tmp = [1 for _ in range(N)], 1
        for i in range(N):
            output[i] = tmp
            tmp *= nums[i]
        tmp = 1    
        for j in range(N-1, -1, -1):
            output[j] *= tmp
            tmp *= nums[j]
        return output    