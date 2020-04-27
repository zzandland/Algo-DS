class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict or not s: return False
        S = len(s)
        dp = [False if i > 0 else True for i in range(S+1)]
        for i in range(1, S+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[S]            