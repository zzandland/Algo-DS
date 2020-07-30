class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        st = set(wordDict)
        dp = [True] + [False]*N
        for i in range(N):
            for j in range(i, -1, -1):
                if s[j:i+1] in st and dp[j]:
                    dp[i+1] = True
                    break
        return dp[-1]