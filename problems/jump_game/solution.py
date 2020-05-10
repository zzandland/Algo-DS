class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        last = N-1
        for i in range(N-2, -1, -1):
            if i + nums[i] >= last: last = i
        return last == 0        