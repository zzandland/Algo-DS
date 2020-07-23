class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, run: int, tmp: int) -> List[int]:
            if i == len(candidates) or run > target: return []
            if run == target: return [tmp[:]]
            return dfs(i, run + candidates[i], tmp + [candidates[i]]) + dfs(i+1, run, tmp)
        return dfs(0, 0, [])