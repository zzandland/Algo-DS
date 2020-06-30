class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res, i, dic = [], 0, {i: (s, t) for i, s, t in zip(indexes, sources, targets)}
        while i < len(S):
            if i in dic:
                s, t = dic[i]
                if S[i:i+len(s)] == s: res.append(t)
                else: res.append(S[i:i+len(s)])
                i += len(s)
            else:    
                res.append(S[i])
                i += 1
        return ''.join(res)