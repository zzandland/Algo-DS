from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = deque()
        mn = deque()
        l = 0
        res = 0
        for r, rn in enumerate(nums):
            while mx and mx[-1][0] < rn: mx.pop()
            while mn and mn[-1][0] > rn: mn.pop()
            mx.append((rn, r))
            mn.append((rn, r))
            while abs(mx[0][0] - mn[0][0]) > limit:
                l += 1
                while mx[0][1] < l: mx.popleft()
                while mn[0][1] < l: mn.popleft()
            res = max(res, r - l + 1)
        return res