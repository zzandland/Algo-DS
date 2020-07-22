class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return True
        if not wordDict: return False
        st = set(wordDict)
        lgst = max(map(len, wordDict))
        dp = {}
        def dfs(i: int) -> bool:
            if i == len(s): return True
            if i not in dp:
                for j in range(lgst+1):
                    if s[i:i+j+1] in st and dfs(i+j+1):
                        dp[i] = True
                        break
                else:
                    dp[i] = False
            return dp[i]
        return dfs(0)