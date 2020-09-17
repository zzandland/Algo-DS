class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = Counter(t)
        S = Counter()
        def comp() -> bool:
            for c in T:
                if c not in S or S[c] < T[c]: return False
            return True
        l = 0
        res = s + 'A'
        for r, rc in enumerate(s):
            S[rc] += 1
            while comp():
                res = min(res, s[l:r+1], key=len)
                lc = s[l]
                S[lc] -= 1
                if not S[lc]: del S[lc]
                l += 1
                
        return res if res != s + 'A' else ''