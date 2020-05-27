class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        def dfs(i: int, run: List[int]) -> List[List[int]]:
            if i == N: return []
            res = [run]
            for j in range(i+1, N):
                res += dfs(j, run+[nums[j]])
            return res    
        return dfs(-1, [])