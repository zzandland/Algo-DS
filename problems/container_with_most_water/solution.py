import heapq

class Solution:
    def maxArea(self, height: List[int]) -> int:
        H, mx = len(height), 0
        l, r = 0, H-1
        while l < r:
            mx = max(mx, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]: l += 1
            else: r -= 1
        return mx        