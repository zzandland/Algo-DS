class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if nums:
            res += [[nums[i]] + rest for i in range(len(nums)) for rest in self.subsets(nums[i+1:])]
        return res