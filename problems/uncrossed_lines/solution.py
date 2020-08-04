class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = {}
        def dfs(a: int, b: int) -> int:
            if a >= len(A) or b >= len(B): return 0
            if (a, b) not in dp:
                res = 0
                # if a and b same try to connect
                if A[a] == B[b]: res = 1 + dfs(a+1, b+1)
                # otherwise move either a or b
                res = max(res, dfs(a+1, b), dfs(a, b+1))
                dp[a, b] = res
            return dp[a, b]
        
        lena, lenb = len(A), len(B)
        dp = [[0]*(lena+1) for _ in range(lenb+1)]
        for b in range(lenb):
            for a in range(lena):
                tmp = 0
                if A[a] == B[b]: tmp = 1 + dp[b][a]
                tmp = max(tmp, dp[b+1][a], dp[b][a+1])
                dp[b+1][a+1] = tmp
        return dp[lenb][lena]