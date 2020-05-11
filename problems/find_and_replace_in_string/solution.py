class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        if not S or not indexes: return S
        N = len(indexes)
        sort = sorted(zip(indexes, sources, targets), reverse=True)
        for i, s, t in sort:
            if S[i:i+len(s)] == s: S = S[:i] + t + S[i+len(s):]
        return S        