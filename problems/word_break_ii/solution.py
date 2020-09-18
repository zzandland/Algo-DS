class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        st = {*s}
        word2idx = {}
        idx2word = {}
        
        for i, w in enumerate(wordDict):
            st -= {*w}
            word2idx[w] = i
            idx2word[i] = w
        if st: return []
            
        N = len(s)
        dp = [[[]]] + [[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1):
                tmp = s[j:i+1]
                if tmp in word2idx:
                    dp[i+1] += [nxt + [word2idx[tmp]] for nxt in dp[j]]
        return [' '.join(map(lambda x: idx2word[x], arr)) for arr in dp[-1]]