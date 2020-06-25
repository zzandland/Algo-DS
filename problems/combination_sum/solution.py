class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N, res, run = len(candidates), [], []
        def fn(i: int, s: int) -> None:
            if i == N or s > target: return
            if s == target:
                res.append(run[:])
                return
            for j in range(i, N):
                run.append(candidates[j])
                fn(j, s + candidates[j])
                run.pop()
        fn(0, 0)
        return res