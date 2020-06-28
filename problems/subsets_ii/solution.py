class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        def dq(i: int) -> List[List[int]]:
            if i == N: return []
            res = []
            for j in range(i, N):
                n = nums[j]
                if j > i and n == nums[j-1]: continue
                res.append([n])
                for st in dq(j+1):
                    res.append([n] + st)
            return res
        return dq(0) + [[]]