class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            ln = len(res)
            for i in range(ln):
                res.append(res[i] + [n])
        return res