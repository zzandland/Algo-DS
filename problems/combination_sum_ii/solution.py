class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N, res, run = len(candidates), [], []
        def bt(i: int, s: int) -> None:
            if s > target: return
            if s == target:
                res.append(run[:])
                return
            for j in range(i, N):
                if j > i and candidates[j] == candidates[j-1]: continue
                run.append(candidates[j])
                bt(j+1, s + candidates[j])
                run.pop()
        bt(0, 0)
        return res