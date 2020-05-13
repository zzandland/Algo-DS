class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        f, t = [set() for _ in range(N+1)], [set() for _ in range(N+1)]
        for frm, to in trust:
            f[frm].add(to)
            t[to].add(frm)
        for i in range(1, N+1):
            if not f[i] and len(t[i]) == N-1: return i
        return -1    