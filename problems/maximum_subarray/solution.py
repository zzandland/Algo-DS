class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return float('-inf')
        mx = r = nums[0]
        for i in range(1, len(nums)):
            mx += nums[i]
            if mx < nums[i]:
                mx = nums[i]
            r = max(mx, r)    
        return r    