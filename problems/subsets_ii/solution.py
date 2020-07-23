class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        def dfs(i: int, tmp: List[int]) -> List[int]:
            res = [tmp[:]]
            for j in range(i, N):
                if j > i and nums[j] == nums[j-1]: continue
                res += dfs(j+1, tmp+[nums[j]])
            return res
        return dfs(0, [])