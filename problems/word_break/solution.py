class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        S, ws = len(s), set(wordDict)
        trues = [0]
        for i in range(1, S+1):
            for j in range(len(trues)-1, -1, -1):
                if s[trues[j]:i] in ws:
                    trues.append(i)
                    break
        return trues[-1] == S