class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        seen = set()
        res = []
        def dfs(i: int, run: int, tmp: List[int]) -> None:
            if run == target: return [tmp]
            elif run < target:
                res = []
                for j in range(i, N):
                    if j > i and candidates[j] == candidates[j-1]: continue
                    res += dfs(j+1, run + candidates[j], tmp + [candidates[j]])
                return res
            return []
        return dfs(0, 0, [])