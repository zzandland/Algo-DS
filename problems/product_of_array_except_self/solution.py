class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res, run = [1]*N, 1
        for i in range(1, N):
            res[i] = nums[i-1] * res[i-1]
        for j in range(N-2, -1, -1):
            run *= nums[j+1]
            res[j] *= run
        return res    