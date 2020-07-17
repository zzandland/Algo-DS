from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx, mn = deque(), deque()
        l = res = 0
        for r, num in enumerate(nums):
            while mx and mx[-1][0] < num: mx.pop()
            while mn and mn[-1][0] > num: mn.pop()
            mx.append((num, r))
            mn.append((num, r))
            if mx[0][0] - mn[0][0] > limit: l += 1
            while mx[0][1] < l: mx.popleft()
            while mn[0][1] < l: mn.popleft()
            res = max(res, r-l+1)
        return res