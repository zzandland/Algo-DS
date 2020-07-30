class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        dic = set()
        letters = set()
        for word in wordDict:
            dic.add(word)
            letters |= set(list(word))
        for c in s:
            if c not in letters: return []
        dp = [[[]]] + [[] for _ in range(N)]
        for i in range(N):
            for j in range(i, -1, -1):
                t = s[j:i+1]
                if t in dic: dp[i+1] += [breaks + [j] for breaks in dp[j]]
        res = []
        for breaks in dp[-1]:
            tmp = []
            breaks.append(N)
            for l, r in zip(breaks, breaks[1:]):
                tmp.append(s[l:r])
            res.append(' '.join(tmp))
        return res