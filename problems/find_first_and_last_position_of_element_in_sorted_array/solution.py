import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        def bs(t: int) -> int:
            l, r = 0, N
            while l < r:
                m = l + (r-l)//2
                if nums[m] < t: l = m+1
                else: r = m
            return l
        l = bs(target)
        if l == N or nums[l] != target: return [-1, -1]
        return [l, bs(target+1)-1]