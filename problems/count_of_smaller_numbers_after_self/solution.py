import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        q = []
        N = len(nums)
        res = [0]*N
        for i in range(N-1, -1, -1):
            bisect.insort_left(q, nums[i])
            idx = bisect.bisect_left(q, nums[i])
            res[i] = idx
        return res