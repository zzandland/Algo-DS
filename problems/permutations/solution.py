class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i, n in enumerate(nums):
            res = [p[:j]+[n]+p[j:] for p in res for j in range(len(p)+1)]
        return res    