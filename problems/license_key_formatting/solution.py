class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.replace('-', '')
        r = len(s) % K
        o, s = [s[:r].upper()] if r > 0 else [], s[r:]
        for i in range(0, len(s), K):
            o.append(s[i:i+K].upper())
        return '-'.join(o)    