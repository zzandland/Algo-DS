import heapq

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N, hp, mn, mx, run = len(nums), [], float('inf'), float('-inf'), 0
        for num in nums:
            run += num
            mx = max(mx, run, run-mn)
            mn = min(mn, run)
        return mx    