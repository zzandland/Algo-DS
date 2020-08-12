class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        st = set()
        
        res = []
        for w in words:
            if w:
                N = len(w)
                dp = [True] + [False]*N
                for i in range(N):
                    for j in range(i, -1, -1):
                        if w[j:i+1] in st and dp[j]:
                            dp[i+1] = True
                            break
                if dp[N]: res.append(w)
                st.add(w)
        return res