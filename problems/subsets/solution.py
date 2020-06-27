class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        def dq(i: int) -> List[List[int]]:
            if i == N: return []
            n = nums[i]
            return [[n]] + [[n] + st for st in dq(i+1)] + dq(i+1)
        return [[]] + dq(0)