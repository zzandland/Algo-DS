from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        for w in sorted(words, key=len):
            dp[w] = 1 + max([dp[w[:i] + w[i+1:]] for i in range(len(w))])
        return max(dp.values())