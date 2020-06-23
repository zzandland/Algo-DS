class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S, res = ''.join(S.split('-'))[::-1].upper(), []
        for i in range(0, len(S), K):
            res.append(S[i:i+K])
        return '-'.join(res)[::-1]