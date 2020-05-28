class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        if not nums: return [-1, -1]
        def bs(pos: int) -> int:
            l, r = 0, N-1
            while l < r:
                m = l + (r-l)//2
                if nums[m+pos] == target and nums[m] < nums[m+1]: return m+pos
                if nums[m] <= target-pos: l = m+1
                else: r = m
            return l if nums[l] == target else -1
        return [bs(1), bs(0)]