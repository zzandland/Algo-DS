class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        run, res, dp = [], [], [[None]*N for _ in range(N)]
        def checkPal(l: int, r: int) -> bool:
            if l >= r: return True
            if dp[l][r] == None:
                dp[l][r] = s[l] == s[r] and checkPal(l+1, r-1)
            return dp[l][r]
        def recurse(i: int) -> None:
            if i == N:
                res.append(run[:])
                return
            for j in range(i, N):
                if checkPal(i, j):
                    run.append(s[i:j+1])
                    recurse(j+1)
                    run.pop()
        recurse(0)
        return res