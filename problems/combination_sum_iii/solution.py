class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        run, res = [], []
        def bt(i: int, s: int) -> None:
            if s > n or len(run) > k: return
            if s == n and len(run) == k:
                res.append(run[:])
                return
            for j in range(i, 10):
                run.append(j)
                bt(j+1, s + j)
                run.pop()
        bt(1, 0)
        return res