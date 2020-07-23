class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        idx = 0
        res = []
        while idx < len(nums):
            f, v = nums[idx], nums[idx+1]
            for _ in range(f):
                res.append(v)
            idx += 2
        return res