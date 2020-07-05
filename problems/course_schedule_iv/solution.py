class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False for _1 in range(n)] for _2 in range(n)]
        for u, v in prerequisites:
            dp[u][v] = True
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dp[j][k] = dp[j][k] or (dp[j][i] and dp[i][k])
        return [dp[u][v] for u, v in queries]