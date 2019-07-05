class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums) - 1):
            cnt = max(cnt, nums[i])
            if cnt == 0:
                return False
            cnt -= 1
        return True    