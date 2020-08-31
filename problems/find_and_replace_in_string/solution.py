class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = []
        idx = {i: (s, t) for i, s, t in zip(indexes, sources, targets)}
        p = 0
        for i, (s, t) in sorted(idx.items()):
            if p < i: res.append(S[p:i])
            tmp = S[i:i+len(s)]
            if tmp == s: res.append(t)
            else: res.append(tmp)
            p = i + len(s)
        return ''.join(res + [S[p:]])