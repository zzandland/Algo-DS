class Solution:
    def partition(self, s: str) -> List[List[str]]:
        S = len(s)
        dp = [[False]*S for _ in range(S)]
        for i in range(S-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, S):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] or j-i == 1
                    
        def dfs(i: int, tmp: List[str]) -> List[List[str]]:
            if i == S: return [tmp[:]]
            res = []
            for j in range(i, S):
                if dp[i][j]:
                    tmp.append(s[i:j+1])
                    res += dfs(j+1, tmp)
                    tmp.pop()
            return res
        
        return dfs(0, [])