class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        mn = N-1
        for i in range(N-1, -1, -1):
            if nums[i] + i >= mn: mn = i
        return mn == 0