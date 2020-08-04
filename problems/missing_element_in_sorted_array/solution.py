class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for a, b in zip(nums, nums[1:]):
            missing = b-a-1
            if k > missing: k -= missing
            else: return a + k
        return nums[-1] + k