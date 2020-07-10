from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = l = r = 0
        mx, mn = deque(), deque()
        # go through the pointers O(n)
        while r < len(nums):
            num = nums[r]
            # pop from deque to maintain mx to be monotonically decreasing
            # and mn to be monotonically increasing
            while mx and mx[-1] < num:
                mx.pop()
            while mn and mn[-1] > num:
                mn.pop()
            mx.append(num)
            mn.append(num)
            r += 1
            # popleft achieves removing number from left
            while mx[0] - mn[0] > limit:
                if mx[0] == nums[l]: mx.popleft()
                if mn[0] == nums[l]: mn.popleft()
                l += 1
            res = max(res, r - l)
        return res