class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = 0
        for i, n in enumerate(nums):
            res = max(res, i + n)
            if res >= len(nums) - 1: return True
            if res == i: return False
        return True