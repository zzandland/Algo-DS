class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        wordDictSet = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j : i] in wordDictSet:
                    dp[i] = True
                    break
        return dp[-1]            